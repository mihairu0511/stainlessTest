# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types import LightingSummaryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLightingSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Stainlesstest) -> None:
        lighting_summary = client.lighting_summary.retrieve()
        assert_matches_type(LightingSummaryRetrieveResponse, lighting_summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Stainlesstest) -> None:
        response = client.lighting_summary.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lighting_summary = response.parse()
        assert_matches_type(LightingSummaryRetrieveResponse, lighting_summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Stainlesstest) -> None:
        with client.lighting_summary.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lighting_summary = response.parse()
            assert_matches_type(LightingSummaryRetrieveResponse, lighting_summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLightingSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStainlesstest) -> None:
        lighting_summary = await async_client.lighting_summary.retrieve()
        assert_matches_type(LightingSummaryRetrieveResponse, lighting_summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.lighting_summary.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lighting_summary = await response.parse()
        assert_matches_type(LightingSummaryRetrieveResponse, lighting_summary, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.lighting_summary.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lighting_summary = await response.parse()
            assert_matches_type(LightingSummaryRetrieveResponse, lighting_summary, path=["response"])

        assert cast(Any, response.is_closed) is True
