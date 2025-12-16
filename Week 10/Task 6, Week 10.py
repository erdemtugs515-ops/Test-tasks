########################################################
# Task A10_Tx
# Developer Erdemtugs Odsuren
# Date 2025-12-14
########################################################

import copy
import time
import sys
import os
from typing import Callable

#sorting func
def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
    return PNums

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[0]
    left = [x for x in PNums[1:] if x <= pivot]
    right = [x for x in PNums[1:] if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

#util func
def readValues(PValues: list[int]) -> str:
    PValues.clear()
    filename = input("Insert dataset filename: ")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return ""
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    PValues.append(int(line))
                except ValueError:
                    print(f"Error: Invalid integer '{line}' in file.")
                    return ""
    print(f"Dataset '{filename}' loaded successfully.")
    return filename

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    # if sorting algorithm returns a new list, ignore returned value
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime

def saveResults(PResults: list[str]) -> None:
    filename = input("Insert results filename: ")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    with open(filepath, "w") as f:
        for line in PResults:
            f.write(line + "\n")
    print(f"Results saved in '{filename}'.")


# main menu func


def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    dataset_name: str = ""

    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            dataset_name = readValues(Values)
        elif choice == "2":
            if not Values:
                print("No dataset loaded. Please read dataset first.")
                continue
            if not dataset_name:
                print("Dataset name unknown. Cannot measure speeds.")
                continue

            builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))

            print(f"Measured speeds for dataset '{dataset_name}':")
            print(f" - Built-in sorted {builtin_time} ns")
            print(f" - Buble sort {bubble_time} ns")
            print(f" - Quick sort {quick_time} ns")

            Results = [
                f"Measured speeds for dataset '{dataset_name}':",
                f" - Built-in sorted {builtin_time} ns",
                f" - Buble sort {bubble_time} ns",
                f" - Quick sort {quick_time} ns"
            ]

        elif choice == "3":
            if not Results:
                print("No results to save. Please measure speeds first.")
                continue
            saveResults(Results)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.")

    Values.clear()
    Results.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
