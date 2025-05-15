# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .temperature_zone_status import TemperatureZoneStatus

__all__ = ["TemperatureRetrieveResponse", "Zone"]


class Zone(BaseModel):
    id: int
    """the unique identifier for the zone"""

    name: str

    input_position: Optional[int] = FieldInfo(alias="inputPosition", default=None)

    output_position: Optional[int] = FieldInfo(alias="outputPosition", default=None)

    zone: Optional[str] = None


class TemperatureRetrieveResponse(BaseModel):
    zones: Optional[List[Zone]] = None

    zone_status: Optional[List[TemperatureZoneStatus]] = FieldInfo(alias="zoneStatus", default=None)
