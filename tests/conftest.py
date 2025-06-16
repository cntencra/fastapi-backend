import os
import pytest_asyncio

from fastapi_backend.utils.path_utils import get_project_root
from fastapi_backend.db.psql_connection import open_pool, close_pool
from fastapi_backend.db.seeds.seed import run_seed
from fastapi_backend.db.utils.seed_utils import load_seed_data

test_data_path = get_project_root() / "fastapi_backend" / "db" / "data" / "test_data" / "seed_data.json"

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_environment():
    os.environ["ENV"] = "test"
    await open_pool()
    seed_data = load_seed_data(test_data_path)
    await run_seed(**seed_data.model_dump())
    print("✅ Database seeded.")
    yield
    await close_pool()
    print("🧹 Pool closed.")