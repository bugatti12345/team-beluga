"""empty message

Revision ID: 23872f10cbfd
Revises: e291a2f46ef8
Create Date: 2021-03-31 00:41:38.405529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23872f10cbfd'
down_revision = 'e291a2f46ef8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('google_event_id', sa.String(length=64), nullable=False))
    op.create_unique_constraint(None, 'event_types', ['url'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'event_types', type_='unique')
    op.drop_column('appointments', 'google_event_id')
    # ### end Alembic commands ###
