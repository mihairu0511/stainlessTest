# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.lighting.api_response import APIResponse
from ...types.temperature.heater_retrieve_state_response import HeaterRetrieveStateResponse

__all__ = ["HeaterResource", "AsyncHeaterResource"]


class HeaterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HeaterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return HeaterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HeaterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return HeaterResourceWithStreamingResponse(self)

    def retrieve_state(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HeaterRetrieveStateResponse:
        """
        gets the state of the heater

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/temperature/{zone_id}/heater",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeaterRetrieveStateResponse,
        )

    def set_state(
        self,
        state: Literal["false", "true"],
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        turns the heater on or off

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not state:
            raise ValueError(f"Expected a non-empty value for `state` but received {state!r}")
        return self._post(
            f"/temperature/{zone_id}/heater/{state}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )


class AsyncHeaterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHeaterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return AsyncHeaterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHeaterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return AsyncHeaterResourceWithStreamingResponse(self)

    async def retrieve_state(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HeaterRetrieveStateResponse:
        """
        gets the state of the heater

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/temperature/{zone_id}/heater",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HeaterRetrieveStateResponse,
        )

    async def set_state(
        self,
        state: Literal["false", "true"],
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        turns the heater on or off

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not state:
            raise ValueError(f"Expected a non-empty value for `state` but received {state!r}")
        return await self._post(
            f"/temperature/{zone_id}/heater/{state}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )


class HeaterResourceWithRawResponse:
    def __init__(self, heater: HeaterResource) -> None:
        self._heater = heater

        self.retrieve_state = to_raw_response_wrapper(
            heater.retrieve_state,
        )
        self.set_state = to_raw_response_wrapper(
            heater.set_state,
        )


class AsyncHeaterResourceWithRawResponse:
    def __init__(self, heater: AsyncHeaterResource) -> None:
        self._heater = heater

        self.retrieve_state = async_to_raw_response_wrapper(
            heater.retrieve_state,
        )
        self.set_state = async_to_raw_response_wrapper(
            heater.set_state,
        )


class HeaterResourceWithStreamingResponse:
    def __init__(self, heater: HeaterResource) -> None:
        self._heater = heater

        self.retrieve_state = to_streamed_response_wrapper(
            heater.retrieve_state,
        )
        self.set_state = to_streamed_response_wrapper(
            heater.set_state,
        )


class AsyncHeaterResourceWithStreamingResponse:
    def __init__(self, heater: AsyncHeaterResource) -> None:
        self._heater = heater

        self.retrieve_state = async_to_streamed_response_wrapper(
            heater.retrieve_state,
        )
        self.set_state = async_to_streamed_response_wrapper(
            heater.set_state,
        )
