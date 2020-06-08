"""remove voted column to users

Revision ID: b1cfc85be4eb
Revises: bd3389338eb1
Create Date: 2020-06-07 17:15:23.003537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1cfc85be4eb'
down_revision = 'bd3389338eb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'voted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('voted', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###