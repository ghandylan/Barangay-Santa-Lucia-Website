"""empty message

Revision ID: 271c25817c90
Revises: 7ad4bfe60139
Create Date: 2023-08-02 18:21:18.226089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '271c25817c90'
down_revision = '7ad4bfe60139'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('barangay_official', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=True))

    with op.batch_alter_table('resident', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resident', schema=None) as batch_op:
        batch_op.drop_column('role')

    with op.batch_alter_table('barangay_official', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###