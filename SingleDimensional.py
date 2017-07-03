def get_peak_iteratively(in_nums):
    for element in range(0, len(in_nums) - 1):
        if element == in_nums[0] and element > in_nums[1]:
            return element
        elif element == in_nums[len(in_nums) - 1] and element > in_nums[len(in_nums) - 2]:
            return element
        elif element > in_nums[(len(in_nums) - 1) - 1] and element > in_nums[(len(in_nums) - 1) + 1]:
            return element

    return None


def get_peak_recursively(in_nums):
    current = in_nums[int((len(in_nums) / 2))]
    if len(in_nums) == 1:
        return current
    elif current == in_nums[0] and current >= in_nums[1]:
        return current
    elif current == in_nums[len(in_nums) - 1] and current >= in_nums[len(in_nums) - 2]:
        return current
    elif current < in_nums[int((len(in_nums) / 2)) - 1]:
        in_nums = in_nums[0:int(len(in_nums) / 2)]
        return get_peak_recursively(in_nums)
    else:
        in_nums = in_nums[int(len(in_nums) / 2): len(in_nums) - 1]
        return get_peak_recursively(in_nums)