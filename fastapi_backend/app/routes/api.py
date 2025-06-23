from fastapi import APIRouter
from fastapi_backend.app.controllers.bubble_controllers import BubbleController
from fastapi_backend.app.schemas.db import BubbleDB

router = APIRouter()

@router.get("/bubbles", response_model=list[BubbleDB])   
async def get_bubbles():
    return await BubbleController.list_bubbles()