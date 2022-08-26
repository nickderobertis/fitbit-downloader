# generated by datamodel-codegen:
#   filename:  elevation.json
#   timestamp: 2021-10-31T18:17:22+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class ActivitiesElevationItem(BaseModel):
    dateTime: str
    value: str


class DatasetItem(BaseModel):
    time: str
    value: int


class ActivitiesElevationIntraday(BaseModel):
    dataset: List[DatasetItem]
    datasetInterval: int
    datasetType: str


class ElevationResponse(BaseModel):
    activities_elevation: List[ActivitiesElevationItem] = Field(
        ..., alias="activities-elevation"
    )
    activities_elevation_intraday: ActivitiesElevationIntraday = Field(
        ..., alias="activities-elevation-intraday"
    )
