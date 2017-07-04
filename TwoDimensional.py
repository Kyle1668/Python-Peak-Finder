from random import randint


def get_max(in_nums):
    max_index = current_index = 0

    if len(in_nums) != 1:
        for element in in_nums:
            if element > in_nums[max_index]:
                max_index = current_index

            current_index += 1

    return max_index


def get_2d_peak_recursively(in_nums):
    mid_row = in_nums[int(len(in_nums) / 2)]
    max_index = get_max(mid_row)

    if len(in_nums) == 1:
        return mid_row[max_index]
    elif mid_row == in_nums[0] and mid_row[max_index] > in_nums[1][max_index]:
        return mid_row[max_index]
    elif mid_row == in_nums[len(in_nums) - 1] and mid_row[max_index] > in_nums[len(in_nums) - 2][max_index]:
        return mid_row[max_index]
    elif mid_row[max_index] < in_nums[int(len(in_nums) / 2)][max_index]:
        in_nums = in_nums[0:int(len(in_nums) / 2)]
        return get_2d_peak_recursively(in_nums)
    else:
        in_nums = in_nums[int(len(in_nums) / 2):len(in_nums) - 1]
        return get_2d_peak_recursively(in_nums)