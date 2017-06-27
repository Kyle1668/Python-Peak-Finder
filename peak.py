
def get_peak_iteratively(in_nums):
    peaks = []

    for index in range(len(in_nums)):
        if index == 1 and in_nums[index] > in_nums[index + 1]:
            peaks.append(in_nums[index])
        elif index == len(in_nums) and in_nums[index] > in_nums[index - 1]:
            peaks.append(in_nums[index])
        elif in_nums[index] > in_nums[index - 1] and in_nums[index] > in_nums[index + 1]:
            peaks.append(in_nums[index])

    return peaks


def get_peak_recursively(in_nums):
    current = in_nums[int((len(in_nums) / 2) - 1)]

    if len(in_nums) == 1:
        return current
    elif current < in_nums[(int((len(in_nums) / 2) - 1)) - 1]:
        get_peak_recursively(in_nums[:int((len(in_nums) / 2) - 1)])
    elif current < in_nums[(int((len(in_nums) / 2) - 1)) + 1]:
        get_peak_recursively(in_nums[int((len(in_nums) / 2) - 1):])
    else:
        return current


def test_iterative_approach():
    prompt()
    data = get_nums()
    peak = get_peak_iteratively(data)
    print("\nNumbers:", end=' ')
    print(data)
    print("\nPeak:", end=' ')
    print(peak)


def test_recursive_approach():
    prompt()
    data = get_nums()
    peak = get_peak_recursively(data)
    print("\nNumbers:", end=' ')
    print(data)
    print("\nPeak:", end=' ')
    print(peak)


def prompt():
    print("\nPython Peak Finder!\n")
    print("Enter a series of positive integers.")
    print("Enter \"finish\" to quit.")
    print("__________________________________________\n")


def get_nums():
    num_list = []
    repeat = True

    while repeat:
        print("Enter Number:", end=' ')
        user_input = input()

        if user_input == "done":
            repeat = False
        elif not user_input.isdigit():
            print("Enter positive number.")
        elif int(user_input) <= 0:
            print("Enter positive number.")
        else:
            num_list.append(int(user_input))

    return num_list


def main():
    test_recursive_approach()


main()

