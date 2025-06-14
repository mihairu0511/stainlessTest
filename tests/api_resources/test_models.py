# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainlesstest import Stainlesstest, AsyncStainlesstest
from stainlesstest.types import (
    ModelListResponse,
    PredictionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Stainlesstest) -> None:
        model = client.models.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Stainlesstest) -> None:
        model = client.models.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
            cover_image_url="cover_image_url",
            description="Detect hot dogs in images",
            github_url="https://github.com/alice/hot-dog-detector",
            license_url="license_url",
            paper_url="https://arxiv.org/abs/2504.17639",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Stainlesstest) -> None:
        model = client.models.retrieve(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.retrieve(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.retrieve(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            client.models.with_raw_response.retrieve(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.retrieve(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Stainlesstest) -> None:
        model = client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Stainlesstest) -> None:
        model = client.models.delete(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.delete(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.delete(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            client.models.with_raw_response.delete(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.delete(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_prediction(self, client: Stainlesstest) -> None:
        model = client.models.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
        )
        assert_matches_type(PredictionResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_prediction_with_all_params(self, client: Stainlesstest) -> None:
        model = client.models.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
            stream=True,
            webhook="webhook",
            webhook_events_filter=["start"],
            prefer="wait=5",
        )
        assert_matches_type(PredictionResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_prediction(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(PredictionResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_prediction(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(PredictionResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_prediction(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            client.models.with_raw_response.create_prediction(
                model_name="model_name",
                model_owner="",
                input={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.create_prediction(
                model_name="",
                model_owner="model_owner",
                input={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_readme(self, client: Stainlesstest) -> None:
        model = client.models.get_readme(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_readme(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.get_readme(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_readme(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.get_readme(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(str, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_readme(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            client.models.with_raw_response.get_readme(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.get_readme(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_examples(self, client: Stainlesstest) -> None:
        model = client.models.list_examples(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_examples(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.list_examples(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_examples(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.list_examples(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_examples(self, client: Stainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            client.models.with_raw_response.list_examples(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.models.with_raw_response.list_examples(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip(reason="Prism doesn't support query methods yet")
    @parametrize
    def test_method_search(self, client: Stainlesstest) -> None:
        model = client.models.search(
            body="body",
        )
        assert model is None

    @pytest.mark.skip(reason="Prism doesn't support query methods yet")
    @parametrize
    def test_raw_response_search(self, client: Stainlesstest) -> None:
        response = client.models.with_raw_response.search(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert model is None

    @pytest.mark.skip(reason="Prism doesn't support query methods yet")
    @parametrize
    def test_streaming_response_search(self, client: Stainlesstest) -> None:
        with client.models.with_streaming_response.search(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
            cover_image_url="cover_image_url",
            description="Detect hot dogs in images",
            github_url="https://github.com/alice/hot-dog-detector",
            license_url="license_url",
            paper_url="https://arxiv.org/abs/2504.17639",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.create(
            hardware="cpu",
            name="hot-dog-detector",
            owner="alice",
            visibility="public",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.retrieve(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.delete(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.delete(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.delete(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            await async_client.models.with_raw_response.delete(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.delete(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_prediction(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
        )
        assert_matches_type(PredictionResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_prediction_with_all_params(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
            stream=True,
            webhook="webhook",
            webhook_events_filter=["start"],
            prefer="wait=5",
        )
        assert_matches_type(PredictionResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_prediction(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(PredictionResponse, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_prediction(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.create_prediction(
            model_name="model_name",
            model_owner="model_owner",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(PredictionResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_prediction(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            await async_client.models.with_raw_response.create_prediction(
                model_name="model_name",
                model_owner="",
                input={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.create_prediction(
                model_name="",
                model_owner="model_owner",
                input={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_readme(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.get_readme(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_readme(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.get_readme(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(str, model, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_readme(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.get_readme(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(str, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_readme(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            await async_client.models.with_raw_response.get_readme(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.get_readme(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_examples(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.list_examples(
            model_name="model_name",
            model_owner="model_owner",
        )
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_examples(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.list_examples(
            model_name="model_name",
            model_owner="model_owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert model is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_examples(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.list_examples(
            model_name="model_name",
            model_owner="model_owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_examples(self, async_client: AsyncStainlesstest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_owner` but received ''"):
            await async_client.models.with_raw_response.list_examples(
                model_name="model_name",
                model_owner="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.models.with_raw_response.list_examples(
                model_name="",
                model_owner="model_owner",
            )

    @pytest.mark.skip(reason="Prism doesn't support query methods yet")
    @parametrize
    async def test_method_search(self, async_client: AsyncStainlesstest) -> None:
        model = await async_client.models.search(
            body="body",
        )
        assert model is None

    @pytest.mark.skip(reason="Prism doesn't support query methods yet")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncStainlesstest) -> None:
        response = await async_client.models.with_raw_response.search(
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert model is None

    @pytest.mark.skip(reason="Prism doesn't support query methods yet")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncStainlesstest) -> None:
        async with async_client.models.with_streaming_response.search(
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert model is None

        assert cast(Any, response.is_closed) is True
