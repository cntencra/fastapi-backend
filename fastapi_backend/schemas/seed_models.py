from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from typing import List


class Bubble(BaseModel):
    label: str
    location_x: int
    location_y: int


class Pest(BaseModel):
    pest_name: str


class Visit(BaseModel):
    pest_id: int
    visit_name: Optional[str]
    visit_date: datetime


class Data(BaseModel):
    bubble_id: int
    visit_id: Optional[int]
    value: Optional[int]


class BackgroundImage(BaseModel):
    image_url: str


class Settings(BaseModel):
    no_colors: int
    bubble_size_min: Optional[int]
    bubble_size_max: Optional[int]


class SeedData(BaseModel):
    bubbles: List[Bubble]
    visits: List[Visit]
    pests: List[Pest]
    data: List[Data]
    backgroundimages: List[BackgroundImage]
    settings: List[Settings]
