TIMESTAMP = "Weekday;Hour;Consumption(kWh);Price(€/kWh)"

def readTimestamps(filepath):
    timestamps = []
    with open(filepath, "r") as file:
        next(file) 
        for line in file:
            line = line.strip()
            if line: 
                parts = line.split(";")
               
                parts[2] = float(parts[2])
                parts[3] = float(parts[3])
                timestamps.append(parts)
    return timestamps

def displayTimestamps(timestamps):
    print(TIMESTAMP)
    total_consumption = 0
    total_price = 0
    for t in timestamps:
        print(f"{t[0]};{t[1]};{t[2]};{t[3]}")
        total_consumption += t[2]
        total_price += t[3]
    print(f"Total consumption: {total_consumption}")
    print(f"Total price: {total_price}")