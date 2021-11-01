import pytest

from scheduler.utils import copy_2d_array, get_min


@pytest.mark.parametrize(
    "array, expected",
    [
        [ [[1, 2, 3, 4]], [[1, 2, 3, 4]] ],
        [ [[5, 6], [1]], [[5, 6], [1]] ],
        [ [[None, None], [None, None]], [[None, None], [None, None]] ],
        [ [[0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0], [0, 0, 0, 0]] ]
    ]
)
def test_copy_2d_array(array, expected):
    actual = copy_2d_array(array)
    assert expected == actual


@pytest.mark.parametrize(
    "array, expected",
    [
        [ [[1, 2, 3, 4]], [[0, 0, 0, 0]] ],
        [ [[5, 6], [1]], [[0, 0], [0]] ],
        [ [[None, None], [0, 0]], [[0, 0], [0, 0]] ],
        [ [[0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0], [0, 0, 0, 0]] ]
    ]
)
def test_copy_2d_array_structure_as_zero(array, expected):
    actual = copy_2d_array(array, only_structure=True)
    assert expected == actual


@pytest.mark.parametrize(
    "array, expected",
    [
        [ [[1, 2, 3, 4]], [[None, None, None, None]] ],
        [ [[5, 6], [1]], [[None, None], [None]] ],
        [ [[None, None], [None, None]], [[None, None], [None, None]] ],
        [ [[0, 0, 0], [0, 0, 0, 0]], [[None, None, None], [None, None, None, None]] ]
    ]
)
def test_copy_2d_array_structure_as_none(array, expected):
    actual = copy_2d_array(array, only_structure=True, default_value=None)
    assert expected == actual


@pytest.mark.parametrize(
    "array, expected",
    [
        [[1, 2, 3, 4], 1],
        [[5, 6, 3, 2, 1, 9], 1],
        [[66, 4, 123, 555, 0], 0],
        [[4, 3, 1, 6, 7, 9, 1], 1]
    ]
)
def test_get_min(array, expected):
    actual = get_min(array)
    assert expected == actual
