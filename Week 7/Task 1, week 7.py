print("Program starting.")
print("Collect positive integers.")

numbers = []

while True:
    value = int(input("Insert positive integer(negative stops): "))
    if value < 0:
        break
    numbers.append(value)

print("Stopped collecting positive integers.")

if len(numbers) == 0:
    print("No integers to display.")
else:
    print(f"Displaying {len(numbers)} integers:")
    for index, number in enumerate(numbers):
        print(f"- Index {index} => Ordinal {index + 1} => Integer {number}")

print("Program ending.")
