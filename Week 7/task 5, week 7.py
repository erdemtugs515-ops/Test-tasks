DELIMITER = ";"

class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0

class DAY_USAGE:
    def __init__(self):
        self.weekday = ""
        self.usage = 0.0
        self.cost = 0.0

def readTimestamps(filename):
    timestamps = []
    print(f'Reading file "{filename}".')
    try:
        with open(filename, "r", encoding="utf-8") as file:
            header = True
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if header:
                    header = False
                    continue
                columns = line.split(DELIMITER)
                if len(columns) < 4:
                    continue
                t = TIMESTAMP()
                t.weekday = columns[0]
                t.hour = columns[1]
                t.consumption = float(columns[2])
                t.price = float(columns[3])
                timestamps.append(t)
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
    return timestamps

def analyseTimestamps(timestamps):
    print("Analysing timestamps.")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"]
    results = []
    for day in weekdays:
        day_usage = DAY_USAGE()
        day_usage.weekday = day
        for t in timestamps:
            if t.weekday == day:
                day_usage.usage += t.consumption
                day_usage.cost += t.consumption * t.price
        results.append(day_usage)
    return results

def displayResults(results):
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for r in results:
        print(f" - {r.weekday} usage {r.usage:.2f} kWh, cost {r.cost:.2f} €")
    print("### Electricity consumption summary ###")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = readTimestamps(filename)
    if timestamps:
        results = analyseTimestamps(timestamps)
        displayResults(results)
    print("Program ending.")

if __name__ == "__main__":
    main()