########################################################
# Task A9_T1
# Developer: Erdemtugs Odsuren
# Date 2025-12-13
########################################################

import sys

print("Program starting.")

try:
    exit_code = int(input("Insert exit code (0-255): "))
    if 0 <= exit_code <= 255:
        print("Clean exit")
        sys.exit(exit_code)
    else:
        print("Error: Exit code must be between 0 and 255.")
        sys.exit(1) 
except ValueError:
    print("Error: Please enter a valid integer.")
    sys.exit(1)  
