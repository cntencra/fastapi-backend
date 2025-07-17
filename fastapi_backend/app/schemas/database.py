from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Bubble(BaseModel):
    bubble_id: int
    label: str
    location_x: int
    location_y: int

class Visit(BaseModel):
    visit_id: int
    visit_name: Optional[str]
    visit_date: datetime

class Pest(BaseModel):
    pest_id: int
    pest_name: str