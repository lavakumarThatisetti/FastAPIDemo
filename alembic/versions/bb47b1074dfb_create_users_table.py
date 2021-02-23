"""create users  table

Revision ID: bb47b1074dfb
Revises: 
Create Date: 2021-02-23 16:41:04.976334

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'bb47b1074dfb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('created_on', sa.TIMESTAMP))
    pass


def downgrade():
    pass
