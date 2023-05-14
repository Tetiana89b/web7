from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from baza_2 import Base


def run_migrations_online():

    config = context.config

    fileConfig(config.config_file_name)

    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    Base.metadata.bind = engine

    with engine.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=Base.metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
