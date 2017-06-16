
def prompt():
    print("\nPython Peak Finder!\n")
    print("Enter a series of positive integers.")
    print("Enter \"finish\" to quit.")
    print("__________________________________________\n")


def getnums():
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


def getpeaks(in_nums):
    peaks = []

    for index in range(len(in_nums)):
        if index == 1 and in_nums[index] > in_nums[index + 1]:
            peaks.append(in_nums[index])
        elif index == len(in_nums) and in_nums[index] > in_nums[index - 1]:
            peaks.append(in_nums[index])
        elif in_nums[index] > in_nums[index - 1] and in_nums[index] > in_nums[index + 1]:
            peaks.append(in_nums[index])

    return peaks


def main():
    prompt()
    data = getnums()
    peaks = getpeaks(data)

    print("\nNumbers:", end=' ')
    print(data)
    print("\nPeaks:", end=' ')
    print(peaks)


main()


