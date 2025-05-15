# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SwitchRetrieveResponse"]


class SwitchRetrieveResponse(BaseModel):
    id: Optional[str] = None

    last_update: Optional[datetime] = FieldInfo(alias="lastUpdate", default=None)

    level: Optional[int] = None

    name: Optional[str] = None
