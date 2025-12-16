print("Program starting.")

user_input = input("Insert comma separated integers: ")
values = user_input.split(",")

numbers = []

for value in values:
    value = value.strip()
    try:
        numbers.append(int(value))
    except ValueError:
        print(f"Error: '{value}' is not a valid integer.")

if len(numbers) == 0:
    print("No valid integers to analyze.")
else:
    total = sum(numbers)
    parity = "even" if total % 2 == 0 else "odd"

    print(f"There are {len(numbers)} integers in the list.")
    print(f"Sum of the integers is {total} and it's {parity}")

print("Program ending.")
