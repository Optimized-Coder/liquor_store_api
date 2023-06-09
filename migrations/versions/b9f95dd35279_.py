"""empty message

Revision ID: b9f95dd35279
Revises: 2fd178da77b0
Create Date: 2023-05-04 22:16:54.688660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9f95dd35279'
down_revision = '2fd178da77b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('api_key', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('api_user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_api_user_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_api_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_api_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('api_user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_api_user_username'))
        batch_op.drop_index(batch_op.f('ix_api_user_email'))
        batch_op.drop_index(batch_op.f('ix_api_user_created_at'))

    op.drop_table('api_user')
    # ### end Alembic commands ###
