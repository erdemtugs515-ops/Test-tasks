########################################################
# Task A10_Tx
# Developer Erdemtugs Odsuren
# Date 2025-12-14
########################################################

import sys

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    
    try:
        user_input = input("Insert factorial: ")
        num = int(user_input)
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)
    except ValueError:
        print(f"Error: Could not convert '{user_input}' to integer.")
        sys.exit(1)
    
    result = recursiveFactorial(num)
    print(f"Factorial {num}!\n{num} = {result}")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
