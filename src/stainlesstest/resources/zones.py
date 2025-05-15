# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.zone_list_response import ZoneListResponse

__all__ = ["ZonesResource", "AsyncZonesResource"]


class ZonesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return ZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return ZonesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZoneListResponse:
        return self._get(
            "/zones",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneListResponse,
        )

    def retrieve_quiet(
        self,
        zone_id: Literal["basement", "first-floor", "second-floor"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/quiet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncZonesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#accessing-raw-response-data-eg-headers
        """
        return AsyncZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mihairu0511/stainlessTest#with_streaming_response
        """
        return AsyncZonesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZoneListResponse:
        return await self._get(
            "/zones",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ZoneListResponse,
        )

    async def retrieve_quiet(
        self,
        zone_id: Literal["basement", "first-floor", "second-floor"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/quiet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ZonesResourceWithRawResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.list = to_raw_response_wrapper(
            zones.list,
        )
        self.retrieve_quiet = to_raw_response_wrapper(
            zones.retrieve_quiet,
        )


class AsyncZonesResourceWithRawResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.list = async_to_raw_response_wrapper(
            zones.list,
        )
        self.retrieve_quiet = async_to_raw_response_wrapper(
            zones.retrieve_quiet,
        )


class ZonesResourceWithStreamingResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.list = to_streamed_response_wrapper(
            zones.list,
        )
        self.retrieve_quiet = to_streamed_response_wrapper(
            zones.retrieve_quiet,
        )


class AsyncZonesResourceWithStreamingResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.list = async_to_streamed_response_wrapper(
            zones.list,
        )
        self.retrieve_quiet = async_to_streamed_response_wrapper(
            zones.retrieve_quiet,
        )
