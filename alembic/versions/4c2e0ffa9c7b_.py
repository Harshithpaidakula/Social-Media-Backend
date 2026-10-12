"""empty message

Revision ID: 4c2e0ffa9c7b
Revises: b137e0a99251
Create Date: 2026-10-12 19:44:18.701006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c2e0ffa9c7b'
down_revision: Union[str, Sequence[str], None] = 'b137e0a99251'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
