import pytest

from scheduler.models import Strategy1Model
from scheduler.schedule import Strategy1Planner


strategy1_correct_dataset = [
    pytest.param(
        {
            'field': [
                [0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
            ],
            'task_workload': 5
        },
        [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        id='Straight schedule 1'
    ),
    pytest.param(
        {
            'field': [
                [0, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
            ],
            'task_workload': 2
        },
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        id='Straight schedule 2'
    ),
    pytest.param(
        {
            'field': [
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 1, 1, 0],
            ],
            'task_workload': 2
        },
        [
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
        ],
        id='One migration in the middle'
    ),
    pytest.param(
        {
            'field': [
                [1, 1, 0, 0],
                [1, 0, 1, 1],
                [0, 1, 1, 0],
            ],
            'task_workload': 2
        },
        [
            [0, 0, 1, 1],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
        ],
        id='Second step is migration'
    )
]


@pytest.mark.parametrize("data, expected", strategy1_correct_dataset)
def test_strategy1_planner_working_correctly(data, expected):
    planner = Strategy1Planner(Strategy1Model(**data))
    actual = planner.get_schedule()
    assert expected == actual
