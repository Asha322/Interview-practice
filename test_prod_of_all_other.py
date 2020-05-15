# Find product of all other numbers in an array


def prod_of_others(array):
    if len(array) < 2:
        raise IndexError('Need at least 2 numbers')
    current = 1
    result = [None] * len(array)
    for i in range(len(array)):
        result[i] = current
        current = current * array[i]

    current = 1
    for i in range(len(array) - 1, -1, -1):
        result[i] = result[i] * current
        current = current * array[i]

    return result


def test_small_list():
    actual = prod_of_others([1, 2, 3])
    expected = [6, 3, 2]
    assert (actual == expected)


def test_longer_list():
    actual = prod_of_others([8, 2, 4, 3, 1, 5])
    expected = [120, 480, 240, 320, 960, 192]
    assert (actual == expected)


def test_list_has_one_zero():
    actual = prod_of_others([6, 2, 0, 3])
    expected = [0, 0, 36, 0]
    assert (actual == expected)


def test_one_negative_number():
    actual = prod_of_others([-3, 8, 4])
    expected = [32, -12, -24]
    assert (actual == expected)


def test_all_negative_numbers():
    actual = prod_of_others([-7, -1, -4, -2])
    expected = [-8, -56, -14, -28]
    assert (actual == expected)




