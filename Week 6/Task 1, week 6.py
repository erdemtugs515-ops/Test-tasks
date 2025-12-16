print("Program starting.")
print("This program can read a file.")

filename = input("Insert filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print(f'#### START "{filename}" ####')
        print(file.read())
        print(f'#### END "{filename}" ####')
except FileNotFoundError:
    print("Error: File not found.")

print("Program ending.")
