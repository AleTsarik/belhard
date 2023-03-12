"""initial

Revision ID: 474284c06abe
Revises: 
Create Date: 2023-03-12 15:48:58.537587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '474284c06abe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('name', sa.VARCHAR(length=24), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('statuses',
    sa.Column('name', sa.VARCHAR(length=10), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('name', sa.VARCHAR(length=24), nullable=True),
    sa.Column('email', sa.VARCHAR(length=24), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('orders',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('status_id', sa.INTEGER(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('title', sa.VARCHAR(length=36), nullable=True),
    sa.Column('description', sa.VARCHAR(length=140), nullable=True),
    sa.Column('category_id', sa.INTEGER(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('order_id', sa.INTEGER(), nullable=True),
    sa.Column('product_id', sa.INTEGER(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('users')
    op.drop_table('statuses')
    op.drop_table('categories')
    # ### end Alembic commands ###
