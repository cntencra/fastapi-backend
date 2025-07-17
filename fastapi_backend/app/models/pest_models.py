from typing import List
from fastapi_backend.db import db_manager
from fastapi_backend.app.schemas.database import Pest

class PestModel():
    @staticmethod
    async def get_all() -> List[Pest]:
        async with db_manager.get_conn() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT pest_id, pest_name FROM pests")
                rows = await cur.fetchall()
                return [
                    Pest(
                        pest_id=row[0],
                        pest_name=row[1]
                        ) for row in rows
                ]