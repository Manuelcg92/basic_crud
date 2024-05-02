"""Migration register

Revision ID: 0ac30946f649
Revises: 8128fb0a8929
Create Date: 2024-05-02 13:15:04.501321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ac30946f649'
down_revision: Union[str, None] = '8128fb0a8929'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    register = op.create_table('register',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('temperatura', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('estacion', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('fecha', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='id_pkey'),
    postgresql_ignore_search_path=False
)


def downgrade() -> None:
    op.drop_table('register')
