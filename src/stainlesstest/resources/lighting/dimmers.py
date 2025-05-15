# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.lighting import dimmer_set_value_with_timer_params
from ...types.lighting.api_response import APIResponse

__all__ = ["DimmersResource", "AsyncDimmersResource"]


class DimmersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DimmersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return DimmersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DimmersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return DimmersResourceWithStreamingResponse(self)

    def set_value(
        self,
        value: int,
        *,
        device_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._post(
            f"/lighting/dimmers/{device_id}/{value}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )

    def set_value_with_timer(
        self,
        timeunit: int,
        *,
        device_id: str,
        value: int,
        units: Literal["seconds", "minutes", "milliseconds"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        sets a dimmer to a specific value on a timer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._post(
            f"/lighting/dimmers/{device_id}/{value}/timer/{timeunit}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"units": units}, dimmer_set_value_with_timer_params.DimmerSetValueWithTimerParams
                ),
            ),
            cast_to=APIResponse,
        )


class AsyncDimmersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDimmersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return AsyncDimmersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDimmersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return AsyncDimmersResourceWithStreamingResponse(self)

    async def set_value(
        self,
        value: int,
        *,
        device_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._post(
            f"/lighting/dimmers/{device_id}/{value}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )

    async def set_value_with_timer(
        self,
        timeunit: int,
        *,
        device_id: str,
        value: int,
        units: Literal["seconds", "minutes", "milliseconds"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        sets a dimmer to a specific value on a timer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._post(
            f"/lighting/dimmers/{device_id}/{value}/timer/{timeunit}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"units": units}, dimmer_set_value_with_timer_params.DimmerSetValueWithTimerParams
                ),
            ),
            cast_to=APIResponse,
        )


class DimmersResourceWithRawResponse:
    def __init__(self, dimmers: DimmersResource) -> None:
        self._dimmers = dimmers

        self.set_value = to_raw_response_wrapper(
            dimmers.set_value,
        )
        self.set_value_with_timer = to_raw_response_wrapper(
            dimmers.set_value_with_timer,
        )


class AsyncDimmersResourceWithRawResponse:
    def __init__(self, dimmers: AsyncDimmersResource) -> None:
        self._dimmers = dimmers

        self.set_value = async_to_raw_response_wrapper(
            dimmers.set_value,
        )
        self.set_value_with_timer = async_to_raw_response_wrapper(
            dimmers.set_value_with_timer,
        )


class DimmersResourceWithStreamingResponse:
    def __init__(self, dimmers: DimmersResource) -> None:
        self._dimmers = dimmers

        self.set_value = to_streamed_response_wrapper(
            dimmers.set_value,
        )
        self.set_value_with_timer = to_streamed_response_wrapper(
            dimmers.set_value_with_timer,
        )


class AsyncDimmersResourceWithStreamingResponse:
    def __init__(self, dimmers: AsyncDimmersResource) -> None:
        self._dimmers = dimmers

        self.set_value = async_to_streamed_response_wrapper(
            dimmers.set_value,
        )
        self.set_value_with_timer = async_to_streamed_response_wrapper(
            dimmers.set_value_with_timer,
        )
