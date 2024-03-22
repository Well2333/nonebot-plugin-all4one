"""init db

Revision ID: 6e6321bc6c48
Revises:
Create Date: 2023-02-20 21:50:33.023674

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "6e6321bc6c48"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_all4one_file",
        sa.Column("headers", sa.JSON(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("src", sa.String(), nullable=True),
        sa.Column("src_id", sa.String(), nullable=True),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("path", sa.String(), nullable=True),
        sa.Column("sha256", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_all4one_file")
    # ### end Alembic commands ###
