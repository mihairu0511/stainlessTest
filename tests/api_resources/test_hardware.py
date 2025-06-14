# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types import HardwareListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHardware:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Stainlesstest) -> None:
        hardware = client.hardware.list()
        assert_matches_type(HardwareListResponse, hardware, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Stainlesstest) -> None:
        response = client.hardware.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hardware = response.parse()
        assert_matches_type(HardwareListResponse, hardware, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Stainlesstest) -> None:
        with client.hardware.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hardware = response.parse()
            assert_matches_type(HardwareListResponse, hardware, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHardware:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncStainlesstest) -> None:
        hardware = await async_client.hardware.list()
        assert_matches_type(HardwareListResponse, hardware, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.hardware.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hardware = await response.parse()
        assert_matches_type(HardwareListResponse, hardware, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.hardware.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hardware = await response.parse()
            assert_matches_type(HardwareListResponse, hardware, path=["response"])

        assert cast(Any, response.is_closed) is True
