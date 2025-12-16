def readValues(filename: str) -> list[float]:
    values = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:  
                    values.append(float(line))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print(f"File '{filename}' contains non-numeric values.")
    return values

def calculateSum(values: list[float]) -> float:
    return round(sum(values), 1)

def calculateAverage(values: list[float]) -> float:
    if not values:
        return 0.0
    return round(sum(values) / len(values), 1)

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def main() -> None:
    print("Program starting.")
    values: list[float] = []

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            filename = input("Insert filename: ").strip()
            values = readValues(filename)
        elif choice == 2:
            print(f"Amount of values {len(values)}")
        elif choice == 3:
            print(f"Sum of values {calculateSum(values)}")
        elif choice == 4:
            print(f"Average of values {calculateAverage(values)}")
        else:
            print("Invalid choice. Please select 0, 1, 2, 3, or 4.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
