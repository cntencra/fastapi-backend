import pytest

from httpx import AsyncClient

pytestmark = pytest.mark.anyio

async def test_not_a_route(async_client: AsyncClient):
    response = await async_client.get("/not_a_route")
    assert response.status_code == 404

async def test_get_bubbles(async_client : AsyncClient):
    response = await async_client.get("/bubbles")
    assert response.status_code == 200
    assert len(response.json()) == 4
    assert isinstance(response.json(), list)

    for bubble in response.json():
        assert isinstance(bubble["bubble_id"], int)
        assert isinstance(bubble["label"], str)
        assert isinstance(bubble["location_x"], int)
        assert isinstance(bubble["location_y"], int)
