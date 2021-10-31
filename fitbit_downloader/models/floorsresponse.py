# generated by datamodel-codegen:
#   filename:  floors.json
#   timestamp: 2021-10-31T18:17:21+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class ActivitiesFloor(BaseModel):
    dateTime: str
    value: str


class DatasetItem(BaseModel):
    time: str
    value: int


class ActivitiesFloorsIntraday(BaseModel):
    dataset: List[DatasetItem]
    datasetInterval: int
    datasetType: str


class FloorsResponse(BaseModel):
    activities_floors: List[ActivitiesFloor] = Field(..., alias='activities-floors')
    activities_floors_intraday: ActivitiesFloorsIntraday = Field(
        ..., alias='activities-floors-intraday'
    )
