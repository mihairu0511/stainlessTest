# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeviceListParams"]


class DeviceListParams(TypedDict, total=False):
    limit: int
    """max number of records to return"""

    skip: int
    """number of records to skip"""
