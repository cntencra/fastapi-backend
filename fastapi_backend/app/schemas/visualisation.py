from pydantic import BaseModel  

class BubbleVisualisation(BaseModel):
    bubble_id: int
    label: str
    location_x: int
    location_y: int
    colour: str
    size: int