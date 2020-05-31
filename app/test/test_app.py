import pytest

from app import api


def test_root():
    response = api.index()
    assert response
    assert "This is the Dad-A-Base api." == response
