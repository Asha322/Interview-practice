# find the rotation point in a sorted rotated array


def find_rotation_point_iterative(input_array):
    start: int = 0
    end = len(input_array) - 1
    while start < end:
        mid = start + ((end - start) // 2)
        if input_array[start] < input_array[mid]:
            start = mid
        else:
            end = mid
    return start + 1


def find_rotation_point_recursive(input_array, start, end):
    if start == end:
        return start
    if start + 1 == end:
        return end
    mid = start + (end - start) // 2
    if input_array[start] < input_array[mid]:
        return find_rotation_point_recursive(input_array, mid, end)
    else:
        return find_rotation_point_recursive(input_array, start, mid)


def test_small_list_iter():
    assert find_rotation_point_iterative(['cape', 'cake']) == 1


def test_medium_list_iter():
    assert find_rotation_point_iterative(['grape', 'orange', 'plum',
                                          'radish', 'apple']) == 4


def test_small_list_recursive():
    assert find_rotation_point_recursive(['cape', 'cake'], 0, 1) == 1


def test_medium_list_recursive():
    assert find_rotation_point_recursive(['grape', 'orange', 'plum',
                                          'radish', 'apple'], 0, 4) == 4
