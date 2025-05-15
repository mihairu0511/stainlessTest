# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TemperatureZoneStatus"]


class TemperatureZoneStatus(BaseModel):
    id: str
    """the unique identifier for the zone"""

    timestamp: datetime
    """the timestamp when the temperature was measured"""

    value: float
    """the temperature in the zone"""

    name: Optional[str] = None
    """the name of the zone"""

    units: Optional[Literal["celsius", "fahrenheit"]] = None
    """the temperature units"""
