########################################################
# Task A10_Tx
# Developer Erdemtugs Odsuren
# Date 2025-12-14
########################################################

import os
import sys

print("Program starting.")

script_dir = os.path.dirname(os.path.abspath(__file__))
filename = input("Insert filename: ")
filepath = os.path.join(script_dir, filename)

if not os.path.exists(filepath):
    print(f"Error: File '{filepath}' does not exist.")
    sys.exit(1)

lines = []
with open(filepath, "r") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:
            lines.append(clean_line)

print("\nVertical display:")
for value in lines:
    print(value)

print("\nHorizontal display:")
print(", ".join(lines))

print("\nProgram ending.")
