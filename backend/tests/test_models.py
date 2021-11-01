import pytest
from pydantic import ValidationError

from scheduler.models import Strategy1Model


strategy1_correct_dataset = [
    pytest.param(
        {
            'field': [
                [0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
            ],
            'completion_time': 5
        },
    ),
    pytest.param(
        {
            'field': [
                [0, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
            ],
            'completion_time': 2
        },
    )
]

strategy1_incorrect_dataset = [
    pytest.param(
        {
            'field': [
                [0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
            ],
            'completion_time': 10
        },
        id='end_x bigger then right border'
    ),
    pytest.param(
        {
            'field': [
                [0, 1, 0, 1],
                [0, 'a', 0, 0],
                [0, 1, 1, 1],
            ],
            'completion_time': 3
        },
        id='one of numbers is string ',
    ),
]


@pytest.mark.parametrize("data", strategy1_correct_dataset)
def test_strategy_1_correct_model(data):
    Strategy1Model(**data)


@pytest.mark.parametrize("data", strategy1_incorrect_dataset)
def test_strategy_1_incorrect_model(data):
    with pytest.raises(ValidationError):
        Strategy1Model(**data)
