from typing import List
from fastapi import HTTPException
from fastapi_backend.app.models.visit_models import VisitModel
from fastapi_backend.app.schemas.database import Data

class VisitController:
    def __init__(self) -> None:
        self.visit_model = VisitModel()
   
    async def get_visits_by_pest_id(self, pest_id: int) -> List[int]:
        visits_by_pest_id  = await self.visit_model.fetch_visits_by_pest_id(pest_id)
        if len(visits_by_pest_id) == 0:
            raise HTTPException(status_code=404, detail=f"Pest with ID {pest_id} not found")
        return visits_by_pest_id
    

    async def get_visit_data(self, visit_id: int, pest_id: int) -> List[Data]:
        visit_data = await self.visit_model.fetch_visit_data(visit_id, pest_id)
        if len(visit_data) == 0:
            raise HTTPException(status_code=404, detail=f"visit_id {visit_id} or pest_id {pest_id} not found")
        return visit_data