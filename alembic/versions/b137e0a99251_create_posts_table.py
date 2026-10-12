"""create posts table

Revision ID: b137e0a99251
Revises: 
Create Date: 2026-10-12 19:30:31.269389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b137e0a99251'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    if not bind.dialect.has_table(bind, "posts"):
        op.create_table(
            "posts",
            sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
            sa.Column("title", sa.String(), nullable=False),
            sa.Column("content", sa.String(), nullable=False),
            sa.Column("published", sa.Boolean(), server_default="true"),
            sa.Column(
                "content_at",
                sa.TIMESTAMP(timezone=True),
                nullable=False,
                server_default=sa.text("now()"),
            ),
            sa.Column("owner_id", sa.Integer(), nullable=False),
        )


def downgrade() -> None:
    op.drop_table('posts')
