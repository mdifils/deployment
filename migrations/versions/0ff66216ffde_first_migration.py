"""First Migration

Revision ID: 0ff66216ffde
Revises: 
Create Date: 2021-09-01 15:49:15.201529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ff66216ffde'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('steam_game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('required_age', sa.Integer(), nullable=True),
    sa.Column('is_free', sa.Boolean(), nullable=False),
    sa.Column('num_reviews', sa.Integer(), nullable=False),
    sa.Column('review_score', sa.Integer(), nullable=False),
    sa.Column('header_image', sa.String(length=400), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('genres', sa.String(length=400), nullable=True),
    sa.Column('categories', sa.String(length=400), nullable=True),
    sa.Column('developers', sa.String(length=400), nullable=True),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('website', sa.String(length=400), nullable=True),
    sa.Column('windows', sa.Boolean(), nullable=True),
    sa.Column('mac', sa.Boolean(), nullable=True),
    sa.Column('linux', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(length=10), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['steam_game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prices')
    op.drop_table('steam_game')
    # ### end Alembic commands ###