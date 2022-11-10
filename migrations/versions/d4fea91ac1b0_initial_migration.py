"""Initial migration.

Revision ID: d4fea91ac1b0
Revises: 
Create Date: 2022-11-10 18:14:30.456940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4fea91ac1b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('idx', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('pwd', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('age', sa.Text(), nullable=False),
    sa.Column('phone', sa.Text(), nullable=True),
    sa.Column('stat', sa.SMALLINT(), nullable=False),
    sa.Column('reg_date', sa.DateTime(timezone='Asia/Seoul'), nullable=False),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('email')
    )
    op.create_table('ranking',
    sa.Column('idx', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_idx', sa.Integer(), nullable=True),
    sa.Column('hint_cnt', sa.Integer(), nullable=False),
    sa.Column('clear_time', sa.Integer(), nullable=False),
    sa.Column('reg_date', sa.DateTime(timezone='Asia/Seoul'), nullable=False),
    sa.ForeignKeyConstraint(['user_idx'], ['users.idx'], ),
    sa.PrimaryKeyConstraint('idx')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ranking')
    op.drop_table('users')
    # ### end Alembic commands ###
