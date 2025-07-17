from fastapi import APIRouter
from fastapi_backend.app.controllers.bubble_controllers import BubbleController
from fastapi_backend.app.controllers.visit_controllers import VisitController
from fastapi_backend.app.controllers.pest_controllers import PestController
from fastapi_backend.app.schemas.database import Bubble, Visit, Pest

router = APIRouter()

@router.get("/bubbles", response_model=list[Bubble])   
async def get_bubbles():
    return await BubbleController.list_bubbles()

@router.get("/visits", response_model=list[Visit])
async def get_visits():
    return await VisitController.list_visits()

@router.get("/pests", response_model=list[Pest])
async def get_pests():
    return await PestController.list_pests()