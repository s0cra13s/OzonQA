from typing import List
from pydantic import BaseModel, Field


class Appearance(BaseModel):
    gender: str
    race: str
    height: List[str]
    weight: List[str]
    eye_color: str = Field(alias='eyeColor')
    hair_color: str = Field(alias='hairColor')


class Work(BaseModel):
    occupation: str
    base: str


class Superhero(BaseModel):
    id: int = Field(ge=1)
    name: str
    appearance: Appearance
    work: Work
