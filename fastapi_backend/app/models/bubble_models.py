from typing import List

from fastapi_backend.db import db_manager
from fastapi_backend.app.schemas.database import Bubble

class BubbleModel():
    @staticmethod
    async def get_all() -> List[Bubble]:
        async with db_manager.get_conn() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT bubble_id, label, location_x, location_y FROM bubbles")
                rows = await cur.fetchall()
                return [
                    Bubble(
                        bubble_id=row[0],
                        label=row[1],
                        location_x=row[2],
                        location_y=row[3]
                    ) for row in rows
                ]