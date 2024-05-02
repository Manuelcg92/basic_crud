"""Migration Users

Revision ID: 8128fb0a8929
Revises: 
Create Date: 2024-05-02 12:52:40.259309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8128fb0a8929'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    users = op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('usuario', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('contraseña', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('usuario', name='usurio_key'),
    postgresql_ignore_search_path=False
)


def downgrade() -> None:
    op.drop_table('users')
