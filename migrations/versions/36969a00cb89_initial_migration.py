"""Initial migration.

Revision ID: 36969a00cb89
Revises:
Create Date: 2022-09-14 13:24:58.889141

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "36969a00cb89"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=128), nullable=False),
        sa.Column("companyName", sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
