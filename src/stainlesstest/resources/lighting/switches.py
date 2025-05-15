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
from ...types.lighting.switch_retrieve_response import SwitchRetrieveResponse

__all__ = ["SwitchesResource", "AsyncSwitchesResource"]


class SwitchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SwitchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#accessing-raw-response-data-eg-headers
        """
        return SwitchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SwitchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#with_streaming_response
        """
        return SwitchesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwitchRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            f"/lighting/switches/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwitchRetrieveResponse,
        )

    def set_value(
        self,
        value: Literal["true", "false"],
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
        if not value:
            raise ValueError(f"Expected a non-empty value for `value` but received {value!r}")
        return self._post(
            f"/lighting/switches/{device_id}/{value}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )

    def set_value_with_timer(
        self,
        minutes: int,
        *,
        device_id: str,
        value: Literal["true", "false"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        sets a switch to a specific value on a timer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not value:
            raise ValueError(f"Expected a non-empty value for `value` but received {value!r}")
        return self._post(
            f"/lighting/switches/{device_id}/{value}/timer/{minutes}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )


class AsyncSwitchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSwitchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSwitchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSwitchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#with_streaming_response
        """
        return AsyncSwitchesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwitchRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            f"/lighting/switches/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SwitchRetrieveResponse,
        )

    async def set_value(
        self,
        value: Literal["true", "false"],
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
        if not value:
            raise ValueError(f"Expected a non-empty value for `value` but received {value!r}")
        return await self._post(
            f"/lighting/switches/{device_id}/{value}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )

    async def set_value_with_timer(
        self,
        minutes: int,
        *,
        device_id: str,
        value: Literal["true", "false"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        sets a switch to a specific value on a timer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        if not value:
            raise ValueError(f"Expected a non-empty value for `value` but received {value!r}")
        return await self._post(
            f"/lighting/switches/{device_id}/{value}/timer/{minutes}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse,
        )


class SwitchesResourceWithRawResponse:
    def __init__(self, switches: SwitchesResource) -> None:
        self._switches = switches

        self.retrieve = to_raw_response_wrapper(
            switches.retrieve,
        )
        self.set_value = to_raw_response_wrapper(
            switches.set_value,
        )
        self.set_value_with_timer = to_raw_response_wrapper(
            switches.set_value_with_timer,
        )


class AsyncSwitchesResourceWithRawResponse:
    def __init__(self, switches: AsyncSwitchesResource) -> None:
        self._switches = switches

        self.retrieve = async_to_raw_response_wrapper(
            switches.retrieve,
        )
        self.set_value = async_to_raw_response_wrapper(
            switches.set_value,
        )
        self.set_value_with_timer = async_to_raw_response_wrapper(
            switches.set_value_with_timer,
        )


class SwitchesResourceWithStreamingResponse:
    def __init__(self, switches: SwitchesResource) -> None:
        self._switches = switches

        self.retrieve = to_streamed_response_wrapper(
            switches.retrieve,
        )
        self.set_value = to_streamed_response_wrapper(
            switches.set_value,
        )
        self.set_value_with_timer = to_streamed_response_wrapper(
            switches.set_value_with_timer,
        )


class AsyncSwitchesResourceWithStreamingResponse:
    def __init__(self, switches: AsyncSwitchesResource) -> None:
        self._switches = switches

        self.retrieve = async_to_streamed_response_wrapper(
            switches.retrieve,
        )
        self.set_value = async_to_streamed_response_wrapper(
            switches.set_value,
        )
        self.set_value_with_timer = async_to_streamed_response_wrapper(
            switches.set_value_with_timer,
        )
