########################################################
# Task A10_Tx
# Developer Erdemtugs Odsuren
# Date 2025-12-14
########################################################

import sys
import os

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = 0
    PMerge.clear()
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    while i < len(PLeft):
        PMerge.append(PLeft[i])
        i += 1
    while j < len(PRight):
        PMerge.append(PRight[j])
        j += 1

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)

def readIntegersFromFile(filename: str) -> list[int]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)

    values = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    values.append(int(line))
                except ValueError:
                    print(f"Error: Invalid integer '{line}' in file.")
                    sys.exit(1)
    return values

def main() -> None:
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    values = readIntegersFromFile(filename)
    print(f"Raw '{filename}' -> {', '.join(map(str, values))}")

    asc_values = values.copy()
    mergeSort(asc_values, PAsc=True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_values))}")

    desc_values = values.copy()
    mergeSort(desc_values, PAsc=False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_values))}")

    print("Program ending.")

if __name__ == "__main__":
    main()
