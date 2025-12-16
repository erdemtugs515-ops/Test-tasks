########################################################
# Task A10_Tx
# Developer Erdemtugs Odsuren
# Date 2025-12-14
########################################################

import sys
import os

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (PAsc and PValues[j] > PValues[j + 1]) or (not PAsc and PValues[j] < PValues[j + 1]):
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
    return None

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
    bubbleSort(asc_values, PAsc=True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_values))}")

    desc_values = values.copy()
    bubbleSort(desc_values, PAsc=False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_values))}")

    print("Program ending.")

if __name__ == "__main__":
    main()
