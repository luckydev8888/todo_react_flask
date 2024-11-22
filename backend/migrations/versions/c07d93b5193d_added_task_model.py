"""added_task_model

Revision ID: c07d93b5193d
Revises: abda7a6fc6af
Create Date: 2024-11-22 00:24:34.005694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c07d93b5193d'
down_revision = 'abda7a6fc6af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.Column('content', sa.String(length=600), nullable=False),
    sa.Column('status', sa.Enum('PENDING', 'IN_PROGRESS', 'COMPLETED', name='taskstatus'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tasks_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_tasks_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tasks_title'))
        batch_op.drop_index(batch_op.f('ix_tasks_created_at'))

    op.drop_table('tasks')
    # ### end Alembic commands ###
