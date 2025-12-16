########################################################
# Task A9_T1
# Developer: Erdemtugs Odsuren
# Date 2025-12-13
########################################################

import sys
import os

print("Program starting.")

filename = input("Insert filename: ")

if not os.path.isfile(filename):
    print(f"Error: File '{filename}' does not exist.")
    sys.exit(1)


print(f"## {filename} ##")
with open(filename, "r") as file:
    print(file.read().strip())
print(f"## {filename} ##")

print("Program ending.")
