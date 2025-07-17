from typing import List
from fastapi_backend.app.schemas.database import Pest
from fastapi_backend.app.models.pest_models import PestModel


class PestController:
    @staticmethod
    async def list_pests() -> List[Pest]:
        pest_model = PestModel()
        pests = await pest_model.get_all()
        return pests