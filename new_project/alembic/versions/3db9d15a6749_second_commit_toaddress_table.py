"""second commit toaddress table

Revision ID: 3db9d15a6749
Revises: e18adbb2dbf6
Create Date: 2022-05-25 17:13:49.362043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3db9d15a6749'
down_revision = 'e18adbb2dbf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vendors')
    op.add_column('address', sa.Column('temporary_addr', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'temporary_addr')
    op.create_table('vendors',
    sa.Column('vendor_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('vendor_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('vendor_id', name='vendors_pkey')
    )
    # ### end Alembic commands ###
