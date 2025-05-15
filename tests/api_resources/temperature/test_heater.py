# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types.lighting import APIResponse
from stainlesstest.types.temperature import HeaterRetrieveStateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHeater:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_state(self, client: Stainlesstest) -> None:
        heater = client.temperature.heater.retrieve_state(
            "zoneId",
        )
        assert_matches_type(HeaterRetrieveStateResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_state(self, client: Stainlesstest) -> None:
        response = client.temperature.heater.with_raw_response.retrieve_state(
            "zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heater = response.parse()
        assert_matches_type(HeaterRetrieveStateResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_state(self, client: Stainlesstest) -> None:
        with client.temperature.heater.with_streaming_response.retrieve_state(
            "zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            heater = response.parse()
            assert_matches_type(HeaterRetrieveStateResponse, heater, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_state(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.temperature.heater.with_raw_response.retrieve_state(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_set_state(self, client: Stainlesstest) -> None:
        heater = client.temperature.heater.set_state(
            state="false",
            zone_id="zoneId",
        )
        assert_matches_type(APIResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_state(self, client: Stainlesstest) -> None:
        response = client.temperature.heater.with_raw_response.set_state(
            state="false",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heater = response.parse()
        assert_matches_type(APIResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_state(self, client: Stainlesstest) -> None:
        with client.temperature.heater.with_streaming_response.set_state(
            state="false",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            heater = response.parse()
            assert_matches_type(APIResponse, heater, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_set_state(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.temperature.heater.with_raw_response.set_state(
                state="false",
                zone_id="",
            )


class TestAsyncHeater:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_state(self, async_client: AsyncStainlesstest) -> None:
        heater = await async_client.temperature.heater.retrieve_state(
            "zoneId",
        )
        assert_matches_type(HeaterRetrieveStateResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_state(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.temperature.heater.with_raw_response.retrieve_state(
            "zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heater = await response.parse()
        assert_matches_type(HeaterRetrieveStateResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_state(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.temperature.heater.with_streaming_response.retrieve_state(
            "zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            heater = await response.parse()
            assert_matches_type(HeaterRetrieveStateResponse, heater, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_state(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.temperature.heater.with_raw_response.retrieve_state(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_state(self, async_client: AsyncStainlesstest) -> None:
        heater = await async_client.temperature.heater.set_state(
            state="false",
            zone_id="zoneId",
        )
        assert_matches_type(APIResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_state(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.temperature.heater.with_raw_response.set_state(
            state="false",
            zone_id="zoneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        heater = await response.parse()
        assert_matches_type(APIResponse, heater, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_state(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.temperature.heater.with_streaming_response.set_state(
            state="false",
            zone_id="zoneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            heater = await response.parse()
            assert_matches_type(APIResponse, heater, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_set_state(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.temperature.heater.with_raw_response.set_state(
                state="false",
                zone_id="",
            )
