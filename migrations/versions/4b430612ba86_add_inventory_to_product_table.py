"""add inventory to product table

Revision ID: 4b430612ba86
Revises: b9f95dd35279
Create Date: 2023-05-11 20:57:43.991808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b430612ba86'
down_revision = 'b9f95dd35279'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity_in_stock', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('in_stock', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('in_stock')
        batch_op.drop_column('quantity_in_stock')

    # ### end Alembic commands ###
