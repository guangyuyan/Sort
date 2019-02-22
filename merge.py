def merge_sort(array):
    def merge_array(array_l, array_r):
        array = []
        while array_l and array_r:
            if array_l[0] < array_r[0]:
                array.append(array_l.pop(0))
            else:
                array.append(array_r.pop(0))
        if len(array_l) != 0:
            array += array_l
        else:
            array += array_r
        return array

    def recurse_arr(array):
        if len(array) < 2:
            return array
        else:
            mid_idx = len(array) // 2
            array_l = recurse_arr(array[:mid_idx])
            array_r = recurse_arr(array[mid_idx:])

            return merge_array(array_l, array_r)
    return recurse_arr(array)

print(merge_sort([9,6,2,7,1]))