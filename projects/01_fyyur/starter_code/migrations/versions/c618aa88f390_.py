"""empty message

Revision ID: c618aa88f390
Revises: 5edb7603c315
Create Date: 2020-07-18 09:09:07.467735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c618aa88f390'
down_revision = '5edb7603c315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.alter_column('Shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('Shows', 'start_time')
    # ### end Alembic commands ###
