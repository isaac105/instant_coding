"""Add: Users current_round

Revision ID: a4fba1761ac7
Revises: d4fea91ac1b0
Create Date: 2022-11-19 22:24:41.106712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4fba1761ac7'
down_revision = 'd4fea91ac1b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('current_round', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'current_round')
    # ### end Alembic commands ###
