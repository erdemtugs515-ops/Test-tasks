########################################################
# Task A10_Tx
# Developer Erdemtugs Odsuren
# Date 2025-12-14
########################################################

import sys
import os


def readValues(PFilename: str, PValues: list[int]) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, PFilename)

    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)

    with open(filepath, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                try:
                    PValues.append(int(clean_line))
                except ValueError:
                    print(f"Error: Invalid integer '{clean_line}' in file.")
                    sys.exit(1)

def sumOfValues(PValues: list[int]) -> int:
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    product = 1
    for val in PValues:
        product *= val
    return product

def main() -> None:
    Values: list[int] = []
    print("Program starting.")

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    readValues(filename, Values)

    total = sumOfValues(Values)
    prod = productOfValues(Values)

    print("# --- Sum of numbers --- #")
    print(total)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(prod)
    print("# --- Product of numbers --- #")

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
