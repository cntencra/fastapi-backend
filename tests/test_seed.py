import pytest
from fastapi_backend.db.db_manager import DBManager


@pytest.mark.parametrize("table_name", [
    "bubbles",
    "visits",
    "pests",
    "data",
    "backgroundimages",
    "settings"
])
@pytest.mark.asyncio
async def test_tables_exists( db_manager: DBManager, table_name: str):
    async with db_manager.get_conn() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = %s
            );
        """, (table_name,))
      
            exists = await cur.fetchone()
            assert exists is not None, "Query returned no rows"
            assert exists[0], f"Table '{table_name}' does not exist."