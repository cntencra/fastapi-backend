from typing import List
from fastapi_backend.db.db_manager import db_manager
from fastapi_backend.app.schemas.database import  Data

class VisitModel():

    @staticmethod
    async def fetch_visits_by_pest_id(pest_id: int) -> List[int]:
        async with db_manager.get_conn() as conn:
             async with conn.cursor() as cur:
                 await cur.execute("SELECT DISTINCT visit_id FROM data WHERE pest_id=%s",(pest_id,))
                 rows = await cur.fetchall()
                 return [
                     (row[0]) for row in rows
                 ]
             
    @staticmethod
    async def fetch_visit_data(visit_id: int, pest_id: int) -> List[Data]:
        async with db_manager.get_conn() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT data_id, bubble_id, visit_id, value, pest_id  FROM data WHERE visit_id=%s AND pest_id=%s",(visit_id, pest_id,))
                rows = await cur.fetchall()
                return [
                    Data(
                        data_id=row[0],
                        bubble_id=row[1],
                        visit_id=row[2],
                        value=row[3],
                        pest_id=row[4]
                    ) for row in rows
                ]