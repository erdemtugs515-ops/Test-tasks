import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon
import math

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    try:
        x = float(input("- Left edge position: "))
        y = float(input("- Top edge position: "))
        side = float(input("- Side length: "))
    except ValueError:
        print("Invalid numeric input. Square not added.")
        return
    fill = input("- Fill color: ").strip()
    stroke = input("- Stroke color: ").strip()
    PDwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    try:
        cx = float(input("- Center X position: "))
        cy = float(input("- Center Y position: "))
        r = float(input("- Radius: "))
    except ValueError:
        print("Invalid numeric input. Circle not added.")
        return
    fill = input("- Fill color: ").strip()
    stroke = input("- Stroke color: ").strip()
    PDwg.add(Circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))

def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon details:")
    try:
        cx = float(input("Middle point X: "))
        cy = float(input("Middle point Y: "))
        apothem = float(input("Apothem length: "))
    except ValueError:
        print("Invalid numeric input. Hexagon not added.")
        return

    circumradius = apothem / math.cos(math.radians(30))
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.radians(angle_deg)
        x = cx + circumradius * math.cos(angle_rad)
        y = cy + circumradius * math.sin(angle_rad)
        points.append((round(x), round(y)))

    fill = input("Insert fill: ").strip()
    stroke = input("Insert stroke: ").strip()
    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ").strip()
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == "y":
        PDwg.write(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing(size=("500px", "500px"))

    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            drawSquare(Dwg)
        elif choice == 2:
            drawCircle(Dwg)
        elif choice == 3:
            drawHexagon(Dwg)
        elif choice == 4:
            saveSvg(Dwg)
        else:
            print("Invalid choice.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
