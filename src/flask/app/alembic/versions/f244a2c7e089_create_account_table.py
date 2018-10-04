"""create account table

Revision ID: f244a2c7e089
Revises: 
Create Date: 2018-10-04 21:29:15.855659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f244a2c7e089'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_engine1():
    pass


def downgrade_engine1():
    pass


def upgrade_engine2():
    pass


def downgrade_engine2():
    pass

