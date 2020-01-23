# Copyright (C) 2020 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""
update_send_by_default_to_not_null

Create Date: 2020-01-27 11:38:52.899486
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = 'aee19c0a4205'
down_revision = '14891a489a2d'


def update_send_by_default_to_not_null():
  """Alter the column and default value to 1"""
  conn = op.get_bind()
  get_tables = """
  SELECT table_name
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE COLUMN_NAME = 'send_by_default' AND TABLE_SCHEMA='ggrcdev';
  """
  scoped_tables = conn.execute(sa.text(get_tables)).fetchall()

  for name in scoped_tables:
    op.alter_column(name[0], 'send_by_default', existing_type=sa.Boolean,
                    nullable=False, server_default='1')
    table_object = sa.sql.table(
        name[0],
        sa.Column('send_by_default', sa.Boolean),
    )
    conn.execute(sa.sql.update(table_object).where(
        table_object.c.send_by_default is None).values(send_by_default='1'))


def upgrade():
  """Upgrade database schema and/or data, creating a new revision."""
  update_send_by_default_to_not_null()


def downgrade():
  """Downgrade database schema and/or data back to the previous revision."""
  raise NotImplementedError("Downgrade is not supported")
