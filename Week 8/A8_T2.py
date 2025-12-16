import importlib.util
import os

lib_path = os.path.join(os.path.dirname(__file__), "arithmetic_lib.py")
spec = importlib.util.spec_from_file_location("arithmetic_lib", lib_path)
arithmetic_lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arithmetic_lib)

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def askValue(PPrompt: str) -> float:
    while True:
        try:
            return float(input(PPrompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main() -> None:
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.")
            break
        elif choice in [1, 2, 3, 4]:
            num1 = askValue("Insert first value: ")
            num2 = askValue("Insert second value: ")

            if choice == 1:
                print(f"{num1} + {num2} = {arithmetic_lib.add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {arithmetic_lib.subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {arithmetic_lib.multiply(num1, num2)}")
            elif choice == 4:
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"{num1} / {num2} = {arithmetic_lib.divide(num1, num2)}")
        else:
            print("Invalid choice.")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
