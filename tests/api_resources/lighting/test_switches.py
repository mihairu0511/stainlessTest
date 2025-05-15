# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types.lighting import APIResponse, SwitchRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSwitches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Stainlesstest) -> None:
        switch = client.lighting.switches.retrieve(
            "deviceId",
        )
        assert_matches_type(SwitchRetrieveResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Stainlesstest) -> None:
        response = client.lighting.switches.with_raw_response.retrieve(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        switch = response.parse()
        assert_matches_type(SwitchRetrieveResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Stainlesstest) -> None:
        with client.lighting.switches.with_streaming_response.retrieve(
            "deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            switch = response.parse()
            assert_matches_type(SwitchRetrieveResponse, switch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.lighting.switches.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_set_value(self, client: Stainlesstest) -> None:
        switch = client.lighting.switches.set_value(
            value="true",
            device_id="deviceId",
        )
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_value(self, client: Stainlesstest) -> None:
        response = client.lighting.switches.with_raw_response.set_value(
            value="true",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        switch = response.parse()
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_value(self, client: Stainlesstest) -> None:
        with client.lighting.switches.with_streaming_response.set_value(
            value="true",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            switch = response.parse()
            assert_matches_type(APIResponse, switch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_set_value(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.lighting.switches.with_raw_response.set_value(
                value="true",
                device_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_set_value_with_timer(self, client: Stainlesstest) -> None:
        switch = client.lighting.switches.set_value_with_timer(
            minutes=0,
            device_id="deviceId",
            value="true",
        )
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_value_with_timer(self, client: Stainlesstest) -> None:
        response = client.lighting.switches.with_raw_response.set_value_with_timer(
            minutes=0,
            device_id="deviceId",
            value="true",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        switch = response.parse()
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_value_with_timer(self, client: Stainlesstest) -> None:
        with client.lighting.switches.with_streaming_response.set_value_with_timer(
            minutes=0,
            device_id="deviceId",
            value="true",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            switch = response.parse()
            assert_matches_type(APIResponse, switch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_set_value_with_timer(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            client.lighting.switches.with_raw_response.set_value_with_timer(
                minutes=0,
                device_id="",
                value="true",
            )


class TestAsyncSwitches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStainlesstest) -> None:
        switch = await async_client.lighting.switches.retrieve(
            "deviceId",
        )
        assert_matches_type(SwitchRetrieveResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.lighting.switches.with_raw_response.retrieve(
            "deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        switch = await response.parse()
        assert_matches_type(SwitchRetrieveResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.lighting.switches.with_streaming_response.retrieve(
            "deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            switch = await response.parse()
            assert_matches_type(SwitchRetrieveResponse, switch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.lighting.switches.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_value(self, async_client: AsyncStainlesstest) -> None:
        switch = await async_client.lighting.switches.set_value(
            value="true",
            device_id="deviceId",
        )
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_value(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.lighting.switches.with_raw_response.set_value(
            value="true",
            device_id="deviceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        switch = await response.parse()
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_value(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.lighting.switches.with_streaming_response.set_value(
            value="true",
            device_id="deviceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            switch = await response.parse()
            assert_matches_type(APIResponse, switch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_set_value(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.lighting.switches.with_raw_response.set_value(
                value="true",
                device_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        switch = await async_client.lighting.switches.set_value_with_timer(
            minutes=0,
            device_id="deviceId",
            value="true",
        )
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.lighting.switches.with_raw_response.set_value_with_timer(
            minutes=0,
            device_id="deviceId",
            value="true",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        switch = await response.parse()
        assert_matches_type(APIResponse, switch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.lighting.switches.with_streaming_response.set_value_with_timer(
            minutes=0,
            device_id="deviceId",
            value="true",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            switch = await response.parse()
            assert_matches_type(APIResponse, switch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_set_value_with_timer(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
            await async_client.lighting.switches.with_raw_response.set_value_with_timer(
                minutes=0,
                device_id="",
                value="true",
            )
