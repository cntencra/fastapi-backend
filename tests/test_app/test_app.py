import pytest

from httpx import AsyncClient

pytestmark = pytest.mark.anyio

async def test_get_bubbles(async_client : AsyncClient):
    response = await async_client.get("/bubbles")
    assert response.status_code == 200
    assert len(response.json()) == 4