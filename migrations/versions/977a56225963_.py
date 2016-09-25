"""initial

Revision ID: 977a56225963
Revises: None
Create Date: 2016-09-24 22:05:55.701455

"""

# revision identifiers, used by Alembic.
revision = '977a56225963'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('series',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('chapter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('body', sa.String(length=1000000), nullable=True),
    sa.Column('series_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['series_id'], ['series.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chapter')
    op.drop_table('series')
    ### end Alembic commands ###
