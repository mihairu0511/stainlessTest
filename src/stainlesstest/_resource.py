# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
from typing import TYPE_CHECKING

import anyio

if TYPE_CHECKING:
    from ._client import Stainlesstest, AsyncStainlesstest


class SyncAPIResource:
    _client: Stainlesstest

    def __init__(self, client: Stainlesstest) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list
        self._query = client.query

    def _sleep(self, seconds: float) -> None:
        time.sleep(seconds)


class AsyncAPIResource:
    _client: AsyncStainlesstest

    def __init__(self, client: AsyncStainlesstest) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list
        self._query = client.query

    async def _sleep(self, seconds: float) -> None:
        await anyio.sleep(seconds)
