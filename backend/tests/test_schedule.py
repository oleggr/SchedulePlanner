import pytest

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
            'completion_time': 5
        },
        [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        id='Test 1 straight schedule'
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
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        id='Test 2 straight schedule'
    ),
    pytest.param(
        {
            'field': [
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 1, 1, 0],
            ],
            'completion_time': 2
        },
        [
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
        ],
        id='Test not straight schedule'
    )
]


@pytest.mark.skip
@pytest.mark.parametrize("data, expected", strategy1_correct_dataset)
def test_strategy1_planner_working_correctly(data, expected):
    planner = Strategy1Planner(data)
    actual = planner.get_schedule()
    assert expected == actual
