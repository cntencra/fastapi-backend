from typing import List
from fastapi_backend.app.models.bubble_models import BubbleModel
from fastapi_backend.app.schemas.database import Bubble

class BubbleController:
    @staticmethod
    async def list_bubbles() -> List[Bubble]:
        bubble_model = BubbleModel()
        bubbles  = await bubble_model.get_all()
        return bubbles