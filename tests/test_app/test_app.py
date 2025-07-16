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
    for bubble in response.json():
        assert isinstance(bubble["bubble_id"], int)
        assert isinstance(bubble["label"], str)
        assert isinstance(bubble["location_x"], int)
        assert isinstance(bubble["location_y"], int)

async def test_get_pests(async_client: AsyncClient):
    response = await async_client.get("/pests")
    assert response.status_code == 200
    assert len(response.json()) == 2
    for pest in response.json():
        assert isinstance(pest["pest_id"], int)
        assert isinstance(pest["pest_name"], str)


async def test_get_visits_by_pest_id(async_client: AsyncClient):
    response = await async_client.get("/visits/pest/1")
    assert response.status_code == 200
    visits = [1, 2, 3, 4]
    for visit in response.json():
        assert visit["visit_id"] in visits
        visits.remove(visit["visit_id"])

async def test_get_visits_by_pest_id_not_found(async_client: AsyncClient):
    response = await async_client.get("/visits/pest/9999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pest not found"}

async def test_get_visits_by_pest_id_invalid(async_client: AsyncClient):
    response = await async_client.get("/visits/pest/invalid")
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid pest ID format"}

async def test_get_data_by_visit_id(async_client: AsyncClient):
    response = await async_client.get("/visits/1")
    assert response.status_code == 200
    bubble_ids = [1, 2, 3, 4]
    for data in response.json():
        assert data["visit_id"] == 1
        assert data["bubble_id"] in bubble_ids
        bubble_ids.remove(data["bubble_id"])
        assert isinstance(data["value"], int)
        assert data["pest_id"] == 1

async def test_get_data_by_visit_id_not_found(async_client: AsyncClient):
    response = await async_client.get("/visits/9999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Visit not found"}

async def test_get_data_by_visit_id_invalid(async_client: AsyncClient):
    response = await async_client.get("/visits/invalid")
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid visit ID format"}