# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.lighting_summary_retrieve_response import LightingSummaryRetrieveResponse

__all__ = ["LightingSummaryResource", "AsyncLightingSummaryResource"]


class LightingSummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LightingSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return LightingSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LightingSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return LightingSummaryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LightingSummaryRetrieveResponse:
        return self._get(
            "/lightingSummary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LightingSummaryRetrieveResponse,
        )


class AsyncLightingSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLightingSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return AsyncLightingSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLightingSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return AsyncLightingSummaryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LightingSummaryRetrieveResponse:
        return await self._get(
            "/lightingSummary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LightingSummaryRetrieveResponse,
        )


class LightingSummaryResourceWithRawResponse:
    def __init__(self, lighting_summary: LightingSummaryResource) -> None:
        self._lighting_summary = lighting_summary

        self.retrieve = to_raw_response_wrapper(
            lighting_summary.retrieve,
        )


class AsyncLightingSummaryResourceWithRawResponse:
    def __init__(self, lighting_summary: AsyncLightingSummaryResource) -> None:
        self._lighting_summary = lighting_summary

        self.retrieve = async_to_raw_response_wrapper(
            lighting_summary.retrieve,
        )


class LightingSummaryResourceWithStreamingResponse:
    def __init__(self, lighting_summary: LightingSummaryResource) -> None:
        self._lighting_summary = lighting_summary

        self.retrieve = to_streamed_response_wrapper(
            lighting_summary.retrieve,
        )


class AsyncLightingSummaryResourceWithStreamingResponse:
    def __init__(self, lighting_summary: AsyncLightingSummaryResource) -> None:
        self._lighting_summary = lighting_summary

        self.retrieve = async_to_streamed_response_wrapper(
            lighting_summary.retrieve,
        )
