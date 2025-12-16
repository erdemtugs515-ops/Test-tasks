########################################################
# Task A9_T1
# Developer: Erdemtugs Odsuren
# Date 2025-12-13
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    celsius_str = input("Insert Celsius: ")
    try:
        celsius = float(celsius_str)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{celsius_str}'")
    
    if celsius < TEMP_MIN or celsius > TEMP_MAX:
        raise Exception(f"{celsius} temperature out of range.")
    
    return celsius

print("Program starting.")

try:
    temp = collectCelsius()
    print(f"You inserted {temp} °C")
except Exception as e:
    print("Error:", e)
    import sys
    sys.exit(1)

print("Program ending.")
