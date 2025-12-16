print("Program starting.")
print("This program analyses a list of names from a file.")

filename = input("Insert filename to read: ")

print(f'Reading names from "{filename}".')
print("Analysing names...")

try:
    names = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            if name != "": 
                names += name + ";" 
            
    name_list = names.rstrip(";").split(";")

    name_count = len(name_list)
    shortest = min(len(name) for name in name_list)
    longest = max(len(name) for name in name_list)
    average = sum(len(name) for name in name_list) / name_count

    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {name_count}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print("Average name - {:.2f} chars".format(average))
    print("#### REPORT END ####")

except FileNotFoundError:
    print("Error: File not found.")

print("Program ending.")
