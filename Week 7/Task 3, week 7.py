import os

print("Program starting.")

filename = input("Insert filename: ").strip().strip('"')

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, filename)

data_rows = []
results = []

try:
    with open(filepath, "r", encoding="utf-8") as file:
        file.readline()  
        for line in file:
            line = line.strip()
            if line == "":
                continue
            data_rows.append(line)

    def analyse_rows(data_rows, results):
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in weekdays:
            count = 0
            for row in data_rows:
                if row.startswith(day):
                    count += 1
            results.append((day, count))

    def display_results(results):
        print("Analysis results:")
        for day, count in results:
            print(f"{day}: {count} timestamps")

    analyse_rows(data_rows, results)
    display_results(results)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found in script folder.")
except PermissionError:
    print("Error: Permission denied. Is the file open elsewhere?")

print("Program ending.")
