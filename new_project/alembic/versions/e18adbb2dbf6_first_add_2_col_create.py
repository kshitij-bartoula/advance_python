"""first add 2 col create

Revision ID: e18adbb2dbf6
Revises: 
Create Date: 2022-05-25 16:12:30.579309

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e18adbb2dbf6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permanent_addr', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('family',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permanent_addr', sa.String(length=100), nullable=True),
    sa.Column('temporary_addr', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('votes')
    
    op.drop_table('mb_transaction_limit')
    op.drop_table('stock')
    op.drop_table('part_drawings')
    op.drop_table('timesheet_raw')
    op.drop_table('bibek')
    op.drop_table('vendor_parts')
    op.drop_table('sales')
    op.drop_table('buy')
    op.drop_table('customer')
    op.drop_table('basket_b')
    op.drop_table('mb_dfs_deposit_transaction_limit_details')
    op.drop_table('employee_raw')
    op.drop_table('employee')
    op.drop_table('timesheet')
    op.drop_table('equipments')
    op.drop_table('sale')
    op.drop_table('basket_a')
    op.drop_table('parts')
    op.drop_table('product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('product_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('mrp', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('pieces_per_case', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('weight_per_piece', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('uom', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('brand', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('tax_percent', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('updated_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('product_id', name='product_pkey')
    )
    op.create_table('parts',
    sa.Column('part_id', sa.INTEGER(), server_default=sa.text("nextval('parts_part_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('part_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('part_id', name='parts_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('basket_a',
    sa.Column('a', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fruit_a', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('a', name='basket_a_pkey')
    )
    op.create_table('sale',
    sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('volume', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.create_table('equipments',
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('value', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='equipments_pkey')
    )
    op.create_table('timesheet',
    sa.Column('employee_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('department_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('shift_start_time', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('shift_end_time', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.Column('shift_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('shift_type', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('hours_worked', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('attendance', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('has_taken_break', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('break_hour', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('was_charge', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('charge_hour', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('was_on_call', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('on_call_hour', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('num_teammates_absent', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.create_table('employee',
    sa.Column('client_employee_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('department_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('manager_employee_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('salary', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hire_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('term_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('term_reason', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('dob', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('fte', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('fte_status', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('weekly_hours', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('client_employee_id', name='employee_pkey')
    )
    op.create_table('employee_raw',
    sa.Column('employee_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('department_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('department_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('manager_employee_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('employee_role', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('salary', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hire_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('terminated_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('terminated_reason', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('dob', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('fte', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('employee_id', name='employee_raw_pkey')
    )
    op.create_table('mb_dfs_deposit_transaction_limit_details',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('mbdfs_transaction_limit_deposit_request_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('client_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('service_option_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('balance', sa.NUMERIC(precision=19, scale=2), autoincrement=False, nullable=True),
    sa.Column('credit_amount', sa.NUMERIC(precision=19, scale=2), autoincrement=False, nullable=True),
    sa.Column('debit_amount', sa.NUMERIC(precision=19, scale=2), autoincrement=False, nullable=True),
    sa.Column('is_settle', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('last_modified_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('last_modified_by', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('beneficiary_account_no', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('coop_settlement_bank_account_no', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('hub_settlement_bank_account_no', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('originating_transaction_id', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('sender_account_no', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('settlement_id', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('transaction_type', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('dfs_transaction_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='mb_dfs_deposit_transaction_limit_details_pkey')
    )
    op.create_table('basket_b',
    sa.Column('b', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fruit_b', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('b', name='basket_b_pkey')
    )
    op.create_table('customer',
    sa.Column('customer_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('country', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('town', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('customer_id', name='customer_pkey')
    )
    op.create_table('buy',
    sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('volume', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.create_table('sales',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('transaction_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bill_no', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('bill_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('bill_location', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('qty', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('uom', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('gross_price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('tax_pc', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tax_amt', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('discount_pc', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('discount_amt', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('net_bill_amt', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('updated_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='sales_pkey')
    )
    op.create_table('vendor_parts',
    sa.Column('vendor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('part_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['part_id'], ['parts.part_id'], name='vendor_parts_part_id_fkey', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], name='vendor_parts_vendor_id_fkey', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('vendor_id', 'part_id', name='vendor_parts_pkey')
    )
    op.create_table('bibek',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True)
    )
    op.create_table('timesheet_raw',
    sa.Column('employee_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cost_center', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('punch_in_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('punch_out_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('punch_apply_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('hours_worked', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('paycode', sa.VARCHAR(length=255), autoincrement=False, nullable=True)
    )
    op.create_table('part_drawings',
    sa.Column('part_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_extension', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.Column('drawing_data', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['part_id'], ['parts.part_id'], name='part_drawings_part_id_fkey', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('part_id', name='part_drawings_pkey')
    )
    op.create_table('stock',
    sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('balance', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.UniqueConstraint('item_id', name='stock_item_id_key')
    )
    op.create_table('mb_transaction_limit',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('last_modified_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('created_by', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('last_modified_by', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('amount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('reference_id', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('remarks', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('service_option_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('limit_request_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='mb_transaction_limit_pkey')
    )
    op.create_table('votes',
    sa.Column('voter', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('election_year', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('election_type', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.Column('party', sa.VARCHAR(length=3), autoincrement=False, nullable=True)
    )
    op.drop_table('family')
    op.drop_table('address')
    # ### end Alembic commands ###
