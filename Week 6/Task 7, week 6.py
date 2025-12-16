import os
def rot13(text):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += ch
    return result


locations = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace"
}

progress_file = "player_progress.txt"


if not os.path.exists(progress_file):
    with open(progress_file, "w", encoding="utf-8") as f:
        f.write("current_location;next_location;passphrase\n")
        f.write("0;1;qvfpvcyvar\n")


with open(progress_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

last_entry = lines[-1].strip().split(";")
current_location = int(last_entry[0])
next_location = int(last_entry[1])
cipher_passphrase = last_entry[2]

plain_passphrase = rot13(cipher_passphrase)


print("Travel starting.")
print(f"Currently at {locations[current_location]}.")

print(f"Travelling to {locations[next_location]}...")
print(f"...Arriving to the {locations[next_location]}.")
print("Passing the guard at the entrance.")
print(f"\"{plain_passphrase.capitalize()}!\"")

print("Looking for the message in the palace...")
print("Ah, there it is! Seems cryptic.")

cipher_filename = f"{next_location}_{cipher_passphrase}.gkg"

with open(cipher_filename, "r", encoding="utf-8") as f:
    cipher_message = f.readline()

with open(progress_file, "a", encoding="utf-8") as f:
    f.write(cipher_message)

print("[Game] Progress autosaved!")

plain_message = rot13(cipher_message)

plain_filename = f"{next_location}-{plain_passphrase}.txt"
with open(plain_filename, "w", encoding="utf-8") as f:
    f.write(plain_message)

print("Deciphering Emperor's message...")
print("Looks like I've got now the plain version copy of the Emperor's message.")

if next_location < 4:
    new_current = next_location
    new_next = next_location + 1
    new_passphrase = cipher_passphrase 

    with open(progress_file, "a", encoding="utf-8") as f:
        f.write(f"{new_current};{new_next};{new_passphrase}\n")

print("Time to leave...")
print("Travel ending.")
