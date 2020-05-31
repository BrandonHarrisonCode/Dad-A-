import pytest
import json

from app import api


@pytest.fixture()
def client():
    api.api.config["TESTING"] = True
    with api.api.test_client() as client:
        yield client


class TestApp:
    def test_root(self, client):
        response = client.get("/")
        assert response
        assert b"This is the Dad-A-Base api." in response.data

    def test_random(self, client):
        response = client.get("/random")
        assert response
        assert 200 <= response.status_code < 300
        assert response.is_json
        assert response.get_json()["id"]
        assert response.get_json()["joke"]
