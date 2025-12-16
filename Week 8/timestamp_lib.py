from datetime import datetime
import datetime 

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list) -> None:
    PTimestamps.clear()
    try:
        with open(PFilename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    dt = datetime.strptime(line, "%Y-%m-%d %H:%M")
                    PTimestamps.append(dt)
    except FileNotFoundError:
        print(f"File '{PFilename}' not found.")
    except ValueError:
        print(f"File '{PFilename}' contains invalid timestamp formats.")

def calculateYears(PYear: int, PTimestamps: list) -> int:
    count = sum(1 for ts in PTimestamps if ts.year == PYear)
    return count

def calculateMonths(PMonth: str, PTimestamps: list) -> int:
    try:
        month_index = MONTHS.index(PMonth) + 1
    except ValueError:
        return 0
    count = sum(1 for ts in PTimestamps if ts.month == month_index)
    return count

def calculateWeekdays(PWeekday: str, PTimestamps: list) -> int:
    try:
        weekday_index = WEEKDAYS.index(PWeekday)
    except ValueError:
        return 0
    count = sum(1 for ts in PTimestamps if ts.weekday() == weekday_index)
    return count
