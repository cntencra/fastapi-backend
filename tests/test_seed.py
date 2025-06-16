import pytest
from fastapi_backend.db.psql_connection import get_conn


@pytest.mark.parametrize("table_name", [
    "bubbles",
    "visits",
    "pests",
    "data",
    "backgroundimages",
    "settings"
])
@pytest.mark.asyncio
async def test_tables_exists(table_name):
    async with get_conn() as conn:
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
