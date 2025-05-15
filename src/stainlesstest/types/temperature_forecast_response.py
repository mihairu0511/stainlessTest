# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TemperatureForecastResponse", "City", "Value", "ValueTemperature", "ValueWeather"]


class City(BaseModel):
    id: Optional[int] = None

    country: Optional[str] = None

    lat: Optional[float] = None

    lon: Optional[float] = None

    name: Optional[str] = None


class ValueTemperature(BaseModel):
    day: Optional[float] = None

    evening: Optional[float] = None

    high: Optional[float] = None

    low: Optional[float] = None

    morning: Optional[float] = None

    night: Optional[float] = None


class ValueWeather(BaseModel):
    description: Optional[str] = None

    icon: Optional[str] = None

    summary: Optional[str] = None


class Value(BaseModel):
    clouds: Optional[int] = None

    date: Optional[datetime] = None

    humidity: Optional[int] = None

    pressure: Optional[float] = None

    temperature: Optional[ValueTemperature] = None

    weather: Optional[ValueWeather] = None

    wind_speed: Optional[float] = FieldInfo(alias="windSpeed", default=None)


class TemperatureForecastResponse(BaseModel):
    city: Optional[City] = None

    values: Optional[List[Value]] = None
