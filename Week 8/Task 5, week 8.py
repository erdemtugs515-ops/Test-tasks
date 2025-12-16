import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

# lib func

def hashPassword(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def registerUser(username: str, password: str) -> None:
    hashed = hashPassword(password)
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"0{DELIMITER}{username}{DELIMITER}{hashed}\n")
    print("User registration completed!")

def loginUser(username: str, password: str) -> bool:
    hashed = hashPassword(password)
    if not os.path.exists(CREDENTIALS_FILE):
        return False
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(DELIMITER)
                if len(parts) == 3:
                    _, stored_user, stored_hash = parts
                    if stored_user == username and stored_hash == hashed:
                        return True
    return False

# menu func

def showMainMenu() -> None:
    print("\nOptions:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("\nUser Menu:")
    print("1 - View profile")
    print("2 - Change password (not implemented)")
    print("0 - Logout")

# main func

def main() -> None:
    print("Program starting.")
    while True:
        showMainMenu()
        choice = input("Your choice: ").strip()
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            username = input("Insert username: ").strip()
            password = input("Insert password: ").strip()
            if loginUser(username, password):
                print(f"Login successful! Welcome {username}.")
                while True:
                    showUserMenu()
                    u_choice = input("Your choice: ").strip()
                    if u_choice == "0":
                        print(f"{username} logged out.")
                        break
                    elif u_choice == "1":
                        print(f"Username: {username}")
                        print("Password: ******")
                    elif u_choice == "2":
                        print("Change password not implemented.")
                    else:
                        print("Invalid choice.")
            else:
                print("Login failed. Incorrect username or password.")
        elif choice == "2":
            username = input("Insert username: ").strip()
            password = input("Insert password: ").strip()
            registerUser(username, password)
        else:
            print("Invalid choice.")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
