from pydantic import BaseModel

class Bubble(BaseModel):
    bubble_id: int
    label: str
    location_x: int
    location_y: int