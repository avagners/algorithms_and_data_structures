def GenerateBBSTArray(a: list) -> list:

    def array_to_abbst(sorted_array, bbst_array, index):
        middle_index = len(sorted_array) // 2
        bbst_array[index] = sorted_array[middle_index]
        left_subtree = sorted_array[:middle_index]
        if len(left_subtree) > 0:
            left_child_index = 2 * index + 1
            array_to_abbst(left_subtree, bbst_array, left_child_index)
        right_subtree = sorted_array[middle_index+1:]
        if len(right_subtree) > 0:
            right_child_index = 2 * index + 2
            array_to_abbst(right_subtree, bbst_array, right_child_index)
        return bbst_array

    if not a:
        return []
    sorted_array = sorted(a)
    bbst_array = [None] * len(a)
    root_index = 0
    return array_to_abbst(sorted_array, bbst_array, root_index)
