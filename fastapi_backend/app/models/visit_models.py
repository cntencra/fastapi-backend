from typing import List
from fastapi_backend.db import db_manager
from fastapi_backend.app.schemas.db import VisitDB

class VisitModel():
    @staticmethod
    async def get_all() -> List[VisitDB]:
        async with db_manager.get_conn() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT visit_id, visit_name, visit_date FROM visits")
                rows = await cur.fetchall()
                return [
                    VisitDB(
                        visit_id=row[0],
                        visit_name=row[1],
                        visit_date=row[2]
                    ) for row in rows
                ]