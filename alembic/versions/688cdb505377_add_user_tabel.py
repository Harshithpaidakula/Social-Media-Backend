"""add user tabel

Revision ID: 688cdb505377
Revises: 4c2e0ffa9c7b
Create Date: 2026-10-12 21:29:27.534360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '688cdb505377'
down_revision: Union[str, Sequence[str], None] = '4c2e0ffa9c7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "content_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
