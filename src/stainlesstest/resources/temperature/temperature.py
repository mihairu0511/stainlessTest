# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .heater import (
    HeaterResource,
    AsyncHeaterResource,
    HeaterResourceWithRawResponse,
    AsyncHeaterResourceWithRawResponse,
    HeaterResourceWithStreamingResponse,
    AsyncHeaterResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.temperature_forecast_response import TemperatureForecastResponse
from ...types.temperature_retrieve_response import TemperatureRetrieveResponse
from ...types.temperature_zone_status_single_zone import TemperatureZoneStatusSingleZone

__all__ = ["TemperatureResource", "AsyncTemperatureResource"]


class TemperatureResource(SyncAPIResource):
    @cached_property
    def heater(self) -> HeaterResource:
        return HeaterResource(self._client)

    @cached_property
    def with_raw_response(self) -> TemperatureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#accessing-raw-response-data-eg-headers
        """
        return TemperatureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemperatureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#with_streaming_response
        """
        return TemperatureResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemperatureRetrieveResponse:
        return self._get(
            "/temperature",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemperatureRetrieveResponse,
        )

    def forecast(
        self,
        days: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemperatureForecastResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/temperature/forecast/{days}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemperatureForecastResponse,
        )

    def retrieve_by_zone(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemperatureZoneStatusSingleZone:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/temperature/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemperatureZoneStatusSingleZone,
        )


class AsyncTemperatureResource(AsyncAPIResource):
    @cached_property
    def heater(self) -> AsyncHeaterResource:
        return AsyncHeaterResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTemperatureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemperatureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemperatureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#with_streaming_response
        """
        return AsyncTemperatureResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemperatureRetrieveResponse:
        return await self._get(
            "/temperature",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemperatureRetrieveResponse,
        )

    async def forecast(
        self,
        days: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemperatureForecastResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/temperature/forecast/{days}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemperatureForecastResponse,
        )

    async def retrieve_by_zone(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TemperatureZoneStatusSingleZone:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/temperature/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemperatureZoneStatusSingleZone,
        )


class TemperatureResourceWithRawResponse:
    def __init__(self, temperature: TemperatureResource) -> None:
        self._temperature = temperature

        self.retrieve = to_raw_response_wrapper(
            temperature.retrieve,
        )
        self.forecast = to_raw_response_wrapper(
            temperature.forecast,
        )
        self.retrieve_by_zone = to_raw_response_wrapper(
            temperature.retrieve_by_zone,
        )

    @cached_property
    def heater(self) -> HeaterResourceWithRawResponse:
        return HeaterResourceWithRawResponse(self._temperature.heater)


class AsyncTemperatureResourceWithRawResponse:
    def __init__(self, temperature: AsyncTemperatureResource) -> None:
        self._temperature = temperature

        self.retrieve = async_to_raw_response_wrapper(
            temperature.retrieve,
        )
        self.forecast = async_to_raw_response_wrapper(
            temperature.forecast,
        )
        self.retrieve_by_zone = async_to_raw_response_wrapper(
            temperature.retrieve_by_zone,
        )

    @cached_property
    def heater(self) -> AsyncHeaterResourceWithRawResponse:
        return AsyncHeaterResourceWithRawResponse(self._temperature.heater)


class TemperatureResourceWithStreamingResponse:
    def __init__(self, temperature: TemperatureResource) -> None:
        self._temperature = temperature

        self.retrieve = to_streamed_response_wrapper(
            temperature.retrieve,
        )
        self.forecast = to_streamed_response_wrapper(
            temperature.forecast,
        )
        self.retrieve_by_zone = to_streamed_response_wrapper(
            temperature.retrieve_by_zone,
        )

    @cached_property
    def heater(self) -> HeaterResourceWithStreamingResponse:
        return HeaterResourceWithStreamingResponse(self._temperature.heater)


class AsyncTemperatureResourceWithStreamingResponse:
    def __init__(self, temperature: AsyncTemperatureResource) -> None:
        self._temperature = temperature

        self.retrieve = async_to_streamed_response_wrapper(
            temperature.retrieve,
        )
        self.forecast = async_to_streamed_response_wrapper(
            temperature.forecast,
        )
        self.retrieve_by_zone = async_to_streamed_response_wrapper(
            temperature.retrieve_by_zone,
        )

    @cached_property
    def heater(self) -> AsyncHeaterResourceWithStreamingResponse:
        return AsyncHeaterResourceWithStreamingResponse(self._temperature.heater)
