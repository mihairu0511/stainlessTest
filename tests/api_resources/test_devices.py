# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types import DeviceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Stainlesstest) -> None:
        device = client.devices.create()
        assert device is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Stainlesstest) -> None:
        device = client.devices.create(
            id="0729a580-2240-11e6-9eb5-0002a5d5c51b",
            uri="http://10.0.0.220:8080",
        )
        assert device is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Stainlesstest) -> None:
        response = client.devices.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert device is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Stainlesstest) -> None:
        with client.devices.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Stainlesstest) -> None:
        device = client.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Stainlesstest) -> None:
        device = client.devices.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Stainlesstest) -> None:
        response = client.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Stainlesstest) -> None:
        with client.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncStainlesstest) -> None:
        device = await async_client.devices.create()
        assert device is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStainlesstest) -> None:
        device = await async_client.devices.create(
            id="0729a580-2240-11e6-9eb5-0002a5d5c51b",
            uri="http://10.0.0.220:8080",
        )
        assert device is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.devices.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert device is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.devices.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncStainlesstest) -> None:
        device = await async_client.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStainlesstest) -> None:
        device = await async_client.devices.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True
