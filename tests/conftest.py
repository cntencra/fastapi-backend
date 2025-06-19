import os
import pytest_asyncio
from typing import AsyncGenerator

from fastapi_backend.db import db_manager, DBManager
from fastapi_backend.utils.path_utils import get_project_root
from fastapi_backend.db.utils.seed_utils import load_seed_data
from fastapi_backend.db.seeds.seed import seed

@pytest_asyncio.fixture(scope="session")
async def db_manager_fixture() -> AsyncGenerator[DBManager, None]: 
    test_data_path = get_project_root() / "fastapi_backend" / "db" / "data" / "test_data" / "seed_data.json"
    os.environ["ENV"] = "test"
    await db_manager.open_pool()
    print(f"\n🔗 {os.environ['ENV'].capitalize()} Database connection pool opened.")
    seed_data = load_seed_data(test_data_path)
    await seed(db_manager, seed_data)
    print(f"✅ {os.environ['ENV'].capitalize()} Database seeded.")
    yield db_manager
    await db_manager.close_pool()
    print(f"\n🧹 {os.environ['ENV'].capitalize()} Pool closed.")