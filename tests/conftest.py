import os
import pytest_asyncio

from fastapi_backend.db.db_manager import DBManager
from fastapi_backend.utils.path_utils import get_project_root
from fastapi_backend.db.utils.seed_utils import load_seed_data
from fastapi_backend.db.seeds.seed import run_seed

@pytest_asyncio.fixture(scope="session")
async def db_manager():
    test_data_path = get_project_root() / "fastapi_backend" / "db" / "data" / "test_data" / "seed_data.json"
    os.environ["ENV"] = "test"
    manager = DBManager()
    await manager.open_pool()
    seed_data = load_seed_data(test_data_path)
    await run_seed(manager, **seed_data.model_dump())
    print("✅ Database seeded.")
    yield manager
    await manager.close_pool()
    print("🧹 Pool closed.")