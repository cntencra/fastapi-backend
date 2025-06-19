from fastapi import APIRouter

router = APIRouter()

@router.get("/bubbles")
async def get_bubbles():
    return [ { "label": "1", "location_x": 50, "location_y": 50 }]