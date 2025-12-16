from timestamp_lib import readTimestamps, calculateYears, calculateMonths, calculateWeekdays

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def main() -> None:
    print("Program starting.")
    PTimestamps = []

    filename = input("Insert filename: ").strip()
    readTimestamps(filename, PTimestamps)

    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            try:
                year = int(input("Insert year: "))
                count = calculateYears(year, PTimestamps)
                print(f"Amount of timestamps during year '{year}' is {count}")
            except ValueError:
                print("Invalid year input.")
        elif choice == 2:
            month = input("Insert month: ").strip()
            count = calculateMonths(month, PTimestamps)
            print(f"Amount of timestamps during month '{month}' is {count}")
        elif choice == 3:
            weekday = input("Insert weekday: ").strip()
            count = calculateWeekdays(weekday, PTimestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}")
        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()

#fuck i dont understand tnis at all...