import os
from dotenv import load_dotenv
from psycopg import AsyncConnection 
from psycopg_pool import AsyncConnectionPool
from typing import AsyncGenerator
from contextlib import asynccontextmanager


env_mode = os.getenv("ENV", "dev")
env_file= f".env.{env_mode}"

load_dotenv(env_file)

pg_db = os.getenv("PGDATABASE")
print(f"{env_mode} mode, Connected to database: {pg_db}")

async_pool: AsyncConnectionPool | None = None

async def open_pool():
    global async_pool
    if async_pool is None:
        async_pool = AsyncConnectionPool(open=False)
        await async_pool.open()

async def close_pool():
    global async_pool
    if async_pool is not None:
        await async_pool.close()
        async_pool = None

@asynccontextmanager
async def get_conn() -> AsyncGenerator[AsyncConnection, None]:

    if async_pool is None:
        raise RuntimeError("Database pool has not been initialized")
    async with async_pool.connection() as conn:
        yield conn