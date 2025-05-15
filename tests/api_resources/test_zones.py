# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types import ZoneListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZones:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Stainlesstest) -> None:
        zone = client.zones.list()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Stainlesstest) -> None:
        response = client.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Stainlesstest) -> None:
        with client.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(ZoneListResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_quiet(self, client: Stainlesstest) -> None:
        zone = client.zones.retrieve_quiet(
            "basement",
        )
        assert zone is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_quiet(self, client: Stainlesstest) -> None:
        response = client.zones.with_raw_response.retrieve_quiet(
            "basement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert zone is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_quiet(self, client: Stainlesstest) -> None:
        with client.zones.with_streaming_response.retrieve_quiet(
            "basement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert zone is None

        assert cast(Any, response.is_closed) is True


class TestAsyncZones:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncStainlesstest) -> None:
        zone = await async_client.zones.list()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(ZoneListResponse, zone, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(ZoneListResponse, zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_quiet(self, async_client: AsyncStainlesstest) -> None:
        zone = await async_client.zones.retrieve_quiet(
            "basement",
        )
        assert zone is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_quiet(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.zones.with_raw_response.retrieve_quiet(
            "basement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert zone is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_quiet(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.zones.with_streaming_response.retrieve_quiet(
            "basement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert zone is None

        assert cast(Any, response.is_closed) is True
