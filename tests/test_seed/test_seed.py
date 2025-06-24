import pytest
from fastapi_backend.db import DBManager
from psycopg.rows import dict_row
from psycopg import sql

pytestmark = pytest.mark.anyio

@pytest.mark.parametrize("table_name", [
    "bubbles",
    "visits",
    "pests",
    "data",
    "backgroundimages",
    "settings"
])
async def test_tables_exists(db_manager_fixture: DBManager, table_name: str):
    async with db_manager_fixture.get_conn() as conn:
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

@pytest.mark.parametrize("table_name, column_name, data_type", [
    ("bubbles","bubble_id","integer")
    ,("bubbles","label","character varying")
    ,("bubbles","location_x","integer")
    ,("bubbles","location_y","integer")
    ,("pests","pest_id","integer")
    ,("pests","pest_name","character varying")
    ,("visits","visit_id","integer")
    ,("visits","visit_name","character varying")
    ,("visits","visit_date","timestamp without time zone") 
    ,("data","data_id","integer")
    ,("data","bubble_id","integer")
    ,("data","visit_id","integer")
    ,("data","value","integer")
    ,("data","pest_id","integer")
    ,("backgroundimages","image_id","integer")
    ,("backgroundimages","image_url","text")
    ,("settings","setting_id","integer")
    ,("settings","no_colors","integer")
    ,("settings","bubble_size_min","integer")
    ,("settings","bubble_size_max","integer")
])
async def test_table_column_data_type(db_manager_fixture: DBManager, table_name: str, column_name: str, data_type:str):
    async with db_manager_fixture.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("""
            SELECT *
            FROM information_schema.columns
            WHERE table_name = %s
            AND column_name = %s
                              
            """, (table_name, column_name))

            result = await cur.fetchone()
            assert result is not None, f"{table_name} or {column_name} does not exist."
            assert result["data_type"] == data_type, f"Column '{column_name}' in table '{table_name}' is not of type {data_type}."


@pytest.mark.parametrize("table_name, columns, test_data_length", [
    ("bubbles", ["bubble_id", "label", "location_x", "location_y"],4),
    ("visits", ["visit_id", "visit_name", "visit_date"], 4),
    ("pests", ["pest_id", "pest_name"],2),
    ("data", ["data_id", "bubble_id", "visit_id", "value", "pest_id"],32),
    ("backgroundimages", ["image_id", "image_url"],2),
    ("settings", ["setting_id", "no_colors", "bubble_size_min", "bubble_size_max"],1)
])
async def test_table_has_data(db_manager_fixture: DBManager, table_name: str, columns: list, test_data_length: int):
    async with db_manager_fixture.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            await cur.execute(query)
            rows = await cur.fetchall()
            assert rows, f"Table '{table_name}' is empty."
            assert len(rows) == test_data_length, f"Table '{table_name}' does not have the expected number of rows."
            for row in rows:
                for column in columns:
                    assert column in row, f"Column '{column}' is missing in table '{table_name}'."
                    assert row[column] is not None, f"Column '{column}' in table '{table_name}' has a NULL value."

