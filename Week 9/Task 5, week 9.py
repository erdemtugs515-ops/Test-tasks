########################################################
# Task A9_T1
# Developer: Erdemtugs Odsuren
# Date 2025-12-14
########################################################

def collect_byte(color_name):
    value_str = input(f"Insert {color_name}: ")
    try:
        value = int(value_str)
    except ValueError:
        raise ValueError(f"Invalid {color_name} value")
    if value < 0 or value > 255:
        raise ValueError(f"{color_name} value out of range")
    return value

print("Program starting.")

try:
    r = collect_byte("red")
    g = collect_byte("green")
    b = collect_byte("blue")

    print("RGB Details:")
    print(f"- Red {r}")
    print(f"- Green {g}")
    print(f"- Blue {b}")
    print(f"- Hex #{r:02x}{g:02x}{b:02x}")
    print(f"- RGB(base-10): ({r}, {g}, {b})")
    print(f"- R-byte(base-2): {r:08b}")
    print(f"- G-byte(base-2): {g:08b}")
    print(f"- B-byte(base-2): {b:08b}")

except Exception:
    print("Couldn't perform the designed task due to the invalid input values.")

print("Program ending.")
