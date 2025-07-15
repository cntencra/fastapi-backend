from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class BubbleDB(BaseModel):
    bubble_id: int
    label: str
    location_x: int
    location_y: int

class VisitDB(BaseModel):
    visit_id: int
    visit_name: Optional[str]
    visit_date: datetime