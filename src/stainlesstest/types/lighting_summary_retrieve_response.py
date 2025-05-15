# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LightingSummaryRetrieveResponse", "Zone", "ZoneStatus"]


class Zone(BaseModel):
    id: Optional[str] = None

    device_id: Optional[int] = FieldInfo(alias="deviceId", default=None)

    device_type: Optional[Literal["dimmer", "switch"]] = FieldInfo(alias="deviceType", default=None)

    name: Optional[str] = None

    zone: Optional[str] = None


class ZoneStatus(BaseModel):
    id: Optional[str] = None

    last_update: Optional[datetime] = FieldInfo(alias="lastUpdate", default=None)

    level: Optional[int] = None

    name: Optional[str] = None


class LightingSummaryRetrieveResponse(BaseModel):
    zones: Optional[List[Zone]] = None

    zone_status: Optional[List[ZoneStatus]] = FieldInfo(alias="zoneStatus", default=None)
