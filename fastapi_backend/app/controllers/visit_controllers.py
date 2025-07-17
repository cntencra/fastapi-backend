from typing import List
from fastapi_backend.app.models.visit_models import VisitModel
from fastapi_backend.app.schemas.database import Visit

class VisitController:
    @staticmethod
    async def list_visits() -> List[Visit]:
        visit_model = VisitModel()
        visits  = await visit_model.get_all()
        return visits