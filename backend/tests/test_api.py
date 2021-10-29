import pytest
from fastapi.testclient import TestClient

from scheduler.models import Strategy1ResponseModel


strategy1_input = [
    pytest.param(
        {
            'field': [
                [0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
            ],
            'end_x': 5
        },
        Strategy1ResponseModel(result=[
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]),
        id='Forward path'
    )
]


def test_hello_endpoint(client: TestClient):
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json() == "Hello, world!"


@pytest.mark.parametrize("data, expected", strategy1_input)
def test_strategy_1_endpoint(client: TestClient, data, expected):
    response = client.post('/api/strategy/1', json=data)
    assert response.status_code == 200
    assert response.json() == expected


def test_strategy_2_endpoint(client: TestClient):
    response = client.post('/api/strategy/2')
    assert response.status_code == 200
    assert response.json() == "strategy 2!"


def test_strategy_3_endpoint(client: TestClient):
    response = client.post('/api/strategy/3')
    assert response.status_code == 200
    assert response.json() == "strategy 3!"
