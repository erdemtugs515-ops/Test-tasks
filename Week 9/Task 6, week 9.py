########################################################
# Task A9_T1
# Developer: Erdemtugs Odsuren
# Date 2025-12-14
########################################################

def save_lines_to_file(lines):
    filename = input("Insert filename: ")
    try:
        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"Lines saved to {filename}")
    except Exception as e:
        print("Error saving file:", e)

def main():
    lines = []
    print("Program starting.")
    
    try:
        while True:
            print("\nOptions:")
            print("1 - Insert line")
            print("2 - Save lines")
            print("0 - Exit")
            
            choice = input("Your choice: ")
            
            if choice == "1":
                text = input("Insert text: ")
                lines.append(text)
            elif choice == "2":
                if lines:
                    save_lines_to_file(lines)
                else:
                    print("No lines to save.")
            elif choice == "0":
                if lines:
                    save = input("You have unsaved lines. Save before quit(y/n)?: ").lower()
                    if save == "y":
                        save_lines_to_file(lines)
                break
            else:
                print("Invalid choice. Try again.")
    
    except KeyboardInterrupt:
        print("\nKeyboard interrupt and unsaved progress!")
        if lines:
            save = input("Save before quit(y/n)?: ").lower()
            if save == "y":
                save_lines_to_file(lines)
    
    print("Program ending.")

if __name__ == "__main__":
    main()
