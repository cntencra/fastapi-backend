import os
from dotenv import load_dotenv
from psycopg import AsyncConnection 
from psycopg_pool import AsyncConnectionPool
from typing import AsyncGenerator
from contextlib import asynccontextmanager

class DBManager:

    def __init__ (self):
        env_mode = os.getenv("ENV", "dev")
        env_file= f".env.{env_mode}"

        load_dotenv(env_file)

        self._pg_db = os.getenv("PGDATABASE")
        print(f"{env_mode} mode, Connected to database: {self._pg_db}")

        self._async_pool: AsyncConnectionPool | None = None

    async def open_pool(self):
        if self._async_pool is None:
            self._async_pool = AsyncConnectionPool(open=False)
            await self._async_pool.open()

    async def close_pool(self):
        if self._async_pool is not None:
            await self._async_pool.close()
            self._async_pool = None

    @asynccontextmanager
    async def get_conn(self) -> AsyncGenerator[AsyncConnection, None]:
        if self._async_pool is None:
            raise RuntimeError("Database pool has not been initialized")
        async with self._async_pool.connection() as conn:
            yield conn