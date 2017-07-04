
def get_peak_iteratively(in_nums):
    for index, item in enumerate(in_nums):
        current = in_nums[index]
        if current == in_nums[0] and current > in_nums[1]:
            return current
        elif current == in_nums[len(in_nums) - 1] and current > in_nums[len(in_nums) - 2]:
            return current
        elif current > in_nums[index - 1] and current > in_nums[index+ 1]:
            return current

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
