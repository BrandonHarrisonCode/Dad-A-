import pytest
import json
import psycopg2

from app import database


class TestDatabase:
    def test_valid_init(self):
        database.Database()

    def test_missing_init(self, monkeypatch):
        monkeypatch.delenv("DATABASE_URL")
        with pytest.raises(KeyError):
            database.Database()

    def test_timeout_init(self, monkeypatch):
        monkeypatch.setenv("DATABASE_URL", "postgres://example.com:5432")
        with pytest.raises(psycopg2.OperationalError):
            database.Database()

    def test_get_random(self):
        id, joke = database.Database().get_random_joke()
        assert id
        assert joke
        assert isinstance(id, int)
        assert isinstance(joke, str)
