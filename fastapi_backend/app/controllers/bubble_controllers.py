from typing import List
from fastapi_backend.app.models.bubble_models import BubbleModel
from fastapi_backend.app.schemas.database import Bubble

class BubbleController:
    @staticmethod
    async def get_bubbles() -> List[Bubble]:
        bubble_model = BubbleModel()
        bubbles  = await bubble_model.fetch_bubbles()
        return bubbles