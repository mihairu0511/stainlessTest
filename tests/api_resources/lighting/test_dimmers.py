# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types.lighting import APIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDimmers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_value(self, client: Stainlesstest) -> None:
        dimmer = client.lighting.dimmers.set_value(
            value=0,
            device_id="deviceId",
        )
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_value(self, client: Stainlesstest) -> None:
        response = client.lighting.dimmers.with_raw_response.set_value(
            value=0,
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimmer = response.parse()
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_value(self, client: Stainlesstest) -> None:
        with client.lighting.dimmers.with_streaming_response.set_value(
            value=0,
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimmer = response.parse()
            assert_matches_type(APIResponse, dimmer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_set_value(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.lighting.dimmers.with_raw_response.set_value(
                value=0,
                device_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_set_value_with_timer(self, client: Stainlesstest) -> None:
        dimmer = client.lighting.dimmers.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
        )
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_value_with_timer_with_all_params(self, client: Stainlesstest) -> None:
        dimmer = client.lighting.dimmers.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
            units="seconds",
        )
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_value_with_timer(self, client: Stainlesstest) -> None:
        response = client.lighting.dimmers.with_raw_response.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimmer = response.parse()
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_value_with_timer(self, client: Stainlesstest) -> None:
        with client.lighting.dimmers.with_streaming_response.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimmer = response.parse()
            assert_matches_type(APIResponse, dimmer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_set_value_with_timer(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.lighting.dimmers.with_raw_response.set_value_with_timer(
                timeunit=0,
                device_id="",
                value=0,
            )


class TestAsyncDimmers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_value(self, async_client: AsyncStainlesstest) -> None:
        dimmer = await async_client.lighting.dimmers.set_value(
            value=0,
            device_id="deviceId",
        )
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_value(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.lighting.dimmers.with_raw_response.set_value(
            value=0,
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimmer = await response.parse()
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_value(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.lighting.dimmers.with_streaming_response.set_value(
            value=0,
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimmer = await response.parse()
            assert_matches_type(APIResponse, dimmer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_set_value(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.lighting.dimmers.with_raw_response.set_value(
                value=0,
                device_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        dimmer = await async_client.lighting.dimmers.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
        )
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_value_with_timer_with_all_params(self, async_client: AsyncStainlesstest) -> None:
        dimmer = await async_client.lighting.dimmers.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
            units="seconds",
        )
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.lighting.dimmers.with_raw_response.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimmer = await response.parse()
        assert_matches_type(APIResponse, dimmer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.lighting.dimmers.with_streaming_response.set_value_with_timer(
            timeunit=0,
            device_id="deviceId",
            value=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimmer = await response.parse()
            assert_matches_type(APIResponse, dimmer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.lighting.dimmers.with_raw_response.set_value_with_timer(
                timeunit=0,
                device_id="",
                value=0,
            )
