from fastapi import APIRouter
from fastapi_backend.app.controllers.bubble_controllers import BubbleController
from fastapi_backend.app.controllers.visit_controllers import VisitController
from fastapi_backend.app.controllers.pest_controllers import PestController 
from fastapi_backend.app.schemas.database import Bubble, Visit, Pest, Data

router = APIRouter()

bubble_controller = BubbleController()
visit_controller = VisitController()
pest_controller = PestController()

@router.get("/bubbles", response_model=list[Bubble])   
async def get_bubbles():
    return await bubble_controller.get_bubbles()


@router.get("/visits/pest/{pest_id}", response_model=list[int])
async def get_visits_by_pest_id(pest_id: int):
    return await visit_controller.get_visits_by_pest_id(pest_id)

@router.get("/visit/{visit_id}/pest/{pest_id}", response_model=list[Data])
async def get_visit_data(visit_id: int, pest_id: int):
    return await visit_controller.get_visit_data(visit_id, pest_id)

@router.get("/pests", response_model=list[Pest])
async def get_pests():
    return await pest_controller.get_pests()

