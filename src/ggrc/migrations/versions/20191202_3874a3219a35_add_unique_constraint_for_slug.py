# Copyright (C) 2019 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

"""
add_unique_constraint_for_slug

Create Date: 2019-12-02 16:57:01.987861
"""
# disable Invalid constant name pylint warning for mandatory Alembic variables.
# pylint: disable=invalid-name

from alembic import op


# revision identifiers, used by Alembic.
revision = '3874a3219a35'
down_revision = '007ee00ff963'


def upgrade():
  """Upgrade database schema and/or data, creating a new revision."""
  op.create_unique_constraint('uq_assessment_templates',
                              'assessment_templates',
                              ['slug'])
  op.create_unique_constraint('uq_audits', 'audits',
                              ['slug'])


def downgrade():
  """Downgrade database schema and/or data back to the previous revision."""
  raise NotImplementedError("Downgrade is not supported")
