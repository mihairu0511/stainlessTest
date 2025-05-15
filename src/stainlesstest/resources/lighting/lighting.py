# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dimmers import (
    DimmersResource,
    AsyncDimmersResource,
    DimmersResourceWithRawResponse,
    AsyncDimmersResourceWithRawResponse,
    DimmersResourceWithStreamingResponse,
    AsyncDimmersResourceWithStreamingResponse,
)
from .switches import (
    SwitchesResource,
    AsyncSwitchesResource,
    SwitchesResourceWithRawResponse,
    AsyncSwitchesResourceWithRawResponse,
    SwitchesResourceWithStreamingResponse,
    AsyncSwitchesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LightingResource", "AsyncLightingResource"]


class LightingResource(SyncAPIResource):
    @cached_property
    def dimmers(self) -> DimmersResource:
        return DimmersResource(self._client)

    @cached_property
    def switches(self) -> SwitchesResource:
        return SwitchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> LightingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#accessing-raw-response-data-eg-headers
        """
        return LightingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LightingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#with_streaming_response
        """
        return LightingResourceWithStreamingResponse(self)


class AsyncLightingResource(AsyncAPIResource):
    @cached_property
    def dimmers(self) -> AsyncDimmersResource:
        return AsyncDimmersResource(self._client)

    @cached_property
    def switches(self) -> AsyncSwitchesResource:
        return AsyncSwitchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLightingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLightingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLightingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stainlesstest-python#with_streaming_response
        """
        return AsyncLightingResourceWithStreamingResponse(self)


class LightingResourceWithRawResponse:
    def __init__(self, lighting: LightingResource) -> None:
        self._lighting = lighting

    @cached_property
    def dimmers(self) -> DimmersResourceWithRawResponse:
        return DimmersResourceWithRawResponse(self._lighting.dimmers)

    @cached_property
    def switches(self) -> SwitchesResourceWithRawResponse:
        return SwitchesResourceWithRawResponse(self._lighting.switches)


class AsyncLightingResourceWithRawResponse:
    def __init__(self, lighting: AsyncLightingResource) -> None:
        self._lighting = lighting

    @cached_property
    def dimmers(self) -> AsyncDimmersResourceWithRawResponse:
        return AsyncDimmersResourceWithRawResponse(self._lighting.dimmers)

    @cached_property
    def switches(self) -> AsyncSwitchesResourceWithRawResponse:
        return AsyncSwitchesResourceWithRawResponse(self._lighting.switches)


class LightingResourceWithStreamingResponse:
    def __init__(self, lighting: LightingResource) -> None:
        self._lighting = lighting

    @cached_property
    def dimmers(self) -> DimmersResourceWithStreamingResponse:
        return DimmersResourceWithStreamingResponse(self._lighting.dimmers)

    @cached_property
    def switches(self) -> SwitchesResourceWithStreamingResponse:
        return SwitchesResourceWithStreamingResponse(self._lighting.switches)


class AsyncLightingResourceWithStreamingResponse:
    def __init__(self, lighting: AsyncLightingResource) -> None:
        self._lighting = lighting

    @cached_property
    def dimmers(self) -> AsyncDimmersResourceWithStreamingResponse:
        return AsyncDimmersResourceWithStreamingResponse(self._lighting.dimmers)

    @cached_property
    def switches(self) -> AsyncSwitchesResourceWithStreamingResponse:
        return AsyncSwitchesResourceWithStreamingResponse(self._lighting.switches)
