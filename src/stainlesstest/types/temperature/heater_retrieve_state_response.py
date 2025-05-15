# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["HeaterRetrieveStateResponse"]


class HeaterRetrieveStateResponse(BaseModel):
    id: Optional[str] = None

    state: Optional[str] = None
