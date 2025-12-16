########################################################
# Task A9_T1
# Developer: Erdemtugs Odsuren
# Date 2025-12-13
########################################################

def main():
    print("Program starting.\n")
    total = 0.0

    while True:
        raw_value = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(raw_value)
        except ValueError:
            print(f"Error! '{raw_value}' couldn't be converted to float.")
            continue

        if value == 0:
            break

        total += value

    print(f"\nFinal sum is {total:.2f}")
    print("Program ending.")

if __name__ == "__main__":
    main()
