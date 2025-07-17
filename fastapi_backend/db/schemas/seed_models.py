from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from typing import List


class BubbleDB(BaseModel):
    label: str
    location_x: int
    location_y: int


class PestDB(BaseModel):
    pest_name: str


class VisitDB(BaseModel):
    visit_name: Optional[str]
    visit_date: datetime


class DataDB(BaseModel):
    bubble_id: int
    visit_id: Optional[int]
    value: Optional[int]
    pest_id: int


class BackgroundImageDB(BaseModel):
    image_url: str


class SettingsDB(BaseModel):
    no_colors: int
    bubble_size_min: Optional[int]
    bubble_size_max: Optional[int]


class SeedDataDB(BaseModel):
    bubbles: List[BubbleDB]
    visits: List[VisitDB]
    pests: List[PestDB]
    data: List[DataDB]
    backgroundimages: List[BackgroundImageDB]
    settings: List[SettingsDB]
