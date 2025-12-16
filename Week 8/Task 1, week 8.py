import time

pause_duration = 1.0

print("Program starting.")

while True:
    print("\nOptions:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter 0, 1, or 2.")
        continue

    if choice == 1:
        try:
            pause_duration = float(input("Insert pause duration (s): "))
            print(f"Pause duration set to {pause_duration} seconds.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == 2:
        print(f"Pausing for {pause_duration} seconds.")
        time.sleep(pause_duration)
        print("Unpaused.")
    elif choice == 0:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select 0, 1, or 2.")

print("\nProgram ending.")
