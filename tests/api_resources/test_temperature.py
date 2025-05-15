# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types import (
    TemperatureForecastResponse,
    TemperatureRetrieveResponse,
    TemperatureZoneStatusSingleZone,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemperature:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Stainlesstest) -> None:
        temperature = client.temperature.retrieve()
        assert_matches_type(TemperatureRetrieveResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Stainlesstest) -> None:
        response = client.temperature.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temperature = response.parse()
        assert_matches_type(TemperatureRetrieveResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Stainlesstest) -> None:
        with client.temperature.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temperature = response.parse()
            assert_matches_type(TemperatureRetrieveResponse, temperature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_forecast(self, client: Stainlesstest) -> None:
        temperature = client.temperature.forecast(
            0,
        )
        assert_matches_type(TemperatureForecastResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_forecast(self, client: Stainlesstest) -> None:
        response = client.temperature.with_raw_response.forecast(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temperature = response.parse()
        assert_matches_type(TemperatureForecastResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_forecast(self, client: Stainlesstest) -> None:
        with client.temperature.with_streaming_response.forecast(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temperature = response.parse()
            assert_matches_type(TemperatureForecastResponse, temperature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_zone(self, client: Stainlesstest) -> None:
        temperature = client.temperature.retrieve_by_zone(
            "zoneId",
        )
        assert_matches_type(TemperatureZoneStatusSingleZone, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_zone(self, client: Stainlesstest) -> None:
        response = client.temperature.with_raw_response.retrieve_by_zone(
            "zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temperature = response.parse()
        assert_matches_type(TemperatureZoneStatusSingleZone, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_zone(self, client: Stainlesstest) -> None:
        with client.temperature.with_streaming_response.retrieve_by_zone(
            "zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temperature = response.parse()
            assert_matches_type(TemperatureZoneStatusSingleZone, temperature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_by_zone(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.temperature.with_raw_response.retrieve_by_zone(
                "",
            )


class TestAsyncTemperature:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStainlesstest) -> None:
        temperature = await async_client.temperature.retrieve()
        assert_matches_type(TemperatureRetrieveResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.temperature.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temperature = await response.parse()
        assert_matches_type(TemperatureRetrieveResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.temperature.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temperature = await response.parse()
            assert_matches_type(TemperatureRetrieveResponse, temperature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_forecast(self, async_client: AsyncStainlesstest) -> None:
        temperature = await async_client.temperature.forecast(
            0,
        )
        assert_matches_type(TemperatureForecastResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_forecast(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.temperature.with_raw_response.forecast(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temperature = await response.parse()
        assert_matches_type(TemperatureForecastResponse, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_forecast(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.temperature.with_streaming_response.forecast(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temperature = await response.parse()
            assert_matches_type(TemperatureForecastResponse, temperature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_zone(self, async_client: AsyncStainlesstest) -> None:
        temperature = await async_client.temperature.retrieve_by_zone(
            "zoneId",
        )
        assert_matches_type(TemperatureZoneStatusSingleZone, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_zone(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.temperature.with_raw_response.retrieve_by_zone(
            "zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        temperature = await response.parse()
        assert_matches_type(TemperatureZoneStatusSingleZone, temperature, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_zone(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.temperature.with_streaming_response.retrieve_by_zone(
            "zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            temperature = await response.parse()
            assert_matches_type(TemperatureZoneStatusSingleZone, temperature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_by_zone(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.temperature.with_raw_response.retrieve_by_zone(
                "",
            )
