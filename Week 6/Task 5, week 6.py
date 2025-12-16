SEPARATOR = ";"

def readValues(filename: str) -> str:
    values = ""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                number = line.strip()
                if i < len(lines) - 1:
                    values += number + SEPARATOR
                else:
                    values += number
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
        return ""
    return values

def analyseValues(values_str: str) -> str:
    if not values_str:
        return ""
    numbers = [int(x) for x in values_str.split(SEPARATOR)]
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count
    result = f"Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n"
    return result

def displayResults(filename: str, result: str):
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print(result, end="")
    print("#### Number analysis - END ####")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    result = analyseValues(values)
    displayResults(filename, result)
    print("Program ending.")

if __name__ == "__main__":
    main()