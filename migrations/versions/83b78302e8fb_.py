"""empty message

Revision ID: 83b78302e8fb
Revises: 6b760b8c8bdb
Create Date: 2023-08-02 20:49:28.976247

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '83b78302e8fb'
down_revision = '6b760b8c8bdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resident', schema=None) as batch_op:
        batch_op.alter_column('photo',
               existing_type=sa.BLOB(),
               nullable=True)
        batch_op.alter_column('full_name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('barangay_number',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('sex',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('birthdate',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('relocation_year',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resident', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('relocation_year',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('birthdate',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('sex',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('barangay_number',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('full_name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('photo',
               existing_type=sa.BLOB(),
               nullable=False)

    # ### end Alembic commands ###