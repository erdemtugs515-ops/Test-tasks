########################################################
# Task A10_Tx
# Developer Erdemtugs Odsuren
# Date 2025-12-14
########################################################

import random
import sys
import os

random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    placed = 0
    while placed < PMines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and PMineField[nr][nc] == 9:
                        count += 1
            PMineField[r][c] = count

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0] * PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

def showBoard(PMineField: list[list[int]]) -> None:
    if not PMineField:
        print("No board generated yet.")
        return
    for row in PMineField:
        print(row)

def saveBoard(PMineField: list[list[int]]) -> None:
    if not PMineField:
        print("No board to save.")
        return
    filename = input("Insert filename to save: ")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    with open(filepath, "w") as f:
        for row in PMineField:
            line = ",".join(str(cell) for cell in row)
            f.write(line + "\n")
    print(f"Board saved in '{filename}'.")

def main() -> None:
    PMineField: list[list[int]] = []
    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))
                if mines > rows * cols:
                    print("Error: More mines than total cells.")
                    continue
                generateMinefield(PMineField, rows, cols, mines)
                print("Minefield generated successfully.")
            except ValueError:
                print("Invalid input. Please enter integer values.")
        elif choice == "2":
            showBoard(PMineField)
        elif choice == "3":
            saveBoard(PMineField)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.")

    print("Program ending.")

if __name__ == "__main__":
    main()
