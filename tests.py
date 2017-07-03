
from SingleDimensional import get_peak_iteratively
from SingleDimensional import get_peak_recursively


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