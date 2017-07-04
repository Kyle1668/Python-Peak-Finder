
from SingleDimensional import get_peak_iteratively
from SingleDimensional import get_peak_recursively
from TwoDimensional import get_2d_peak_recursively
from random import randint


def prompt():
    print("\nPython Peak Finder!\n")
    print("__________________________________________\n")


def test_iterative_approach():
    prompt()
    data = [randint(0, 99) for x in range(15)]
    peak = get_peak_iteratively(data)
    print("\nNumbers:", end=' ')
    print(data)
    print("\nPeak:", end=' ')
    print(peak)


def test_recursive_approach():
    prompt()
    data = [randint(0, 99) for x in range(15)]
    peak = get_peak_recursively(data)
    print("\nNumbers:", end=' ')
    print(data)
    print("\nPeak:", end=' ')
    print(peak)


def test_2d_recursive_approach():
    prompt()
    data = [[randint(0, 99) for x in range(5)] for y in range(5)]
    peak = get_2d_peak_recursively(data)
    print("\nNumbers:", end=' ')
    print(data)
    print("\nPeak:", end=' ')
    print(peak)
