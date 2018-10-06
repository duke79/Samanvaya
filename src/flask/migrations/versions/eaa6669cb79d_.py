"""empty message

Revision ID: eaa6669cb79d
Revises: 418f110a45db
Create Date: 2018-10-06 18:04:51.499629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaa6669cb79d'
down_revision = '418f110a45db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('marksheet_post_grad', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'marksheet_post_grad')
    # ### end Alembic commands ###