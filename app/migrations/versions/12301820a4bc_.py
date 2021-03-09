"""empty message

Revision ID: 12301820a4bc
Revises: 8e930f8314bb
Create Date: 2021-03-09 09:40:33.120526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12301820a4bc'
down_revision = '8e930f8314bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Subscription', sa.Column('id2', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Subscription', 'id2')
    # ### end Alembic commands ###
