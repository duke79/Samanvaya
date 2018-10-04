"""Add a column

Revision ID: a90578ba1adb
Revises: f244a2c7e089
Create Date: 2018-10-04 21:35:29.502164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a90578ba1adb'
down_revision = 'f244a2c7e089'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()
    op.drop_column('account', 'last_transaction_date')





def upgrade_engine1():
    pass


def downgrade_engine1():
    pass

