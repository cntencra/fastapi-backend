from fastapi import APIRouter
from fastapi_backend.app.controllers.bubble_controllers import BubbleController
from fastapi_backend.app.controllers.visit_controllers import VisitController   
from fastapi_backend.app.schemas.db import BubbleDB, VisitDB

router = APIRouter()

@router.get("/bubbles", response_model=list[BubbleDB])   
async def get_bubbles():
    return await BubbleController.list_bubbles()

@router.get("/visits", response_model=list[VisitDB])
async def get_visits():
    return await VisitController.list_visits()