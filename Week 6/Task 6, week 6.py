LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def writeFile(Filename: str, Content: str):
    if Filename.strip() == "":
        print("File name not defined.")
        print("Aborting save operation.")
        return
    with open(Filename, "w", encoding="UTF-8") as file:
        file.write(Content)
    print("Ciphered text saved!")

def askRows() -> str:
    print("Collecting plain text rows for ciphering.")
    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        lines.append(row)
    return "\n".join(lines)

def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    if Character in Alphabets:
        index = Alphabets.index(Character)
        return Alphabets[(index + Shift) % len(Alphabets)]
    return Character

def rot13(Content: str) -> str:
    result = ""
    for ch in Content:
        if ch.islower():
            result += shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch.isupper():
            result += shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result += ch
    return result

def main():
    print("Program starting.")
    text = askRows()
    ciphered = rot13(text)
    print("\n#### Ciphered text ####")
    print(ciphered)
    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    if filename.strip():
        writeFile(filename, ciphered)
    else:
        print("File name not defined.")
        print("Aborting save operation.")
    print("Program ending.")

if __name__ == "__main__":
    main()