import random
random.seed(1234)

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = {1: "rock", 2: "paper", 3: "scissors"}
ascii_art = {1: rock_art, 2: paper_art, 3: scissors_art}

scores = {
    "player": {"wins": 0, "losses": 0, "draws": 0},
    "bot": {"wins": 0, "losses": 0, "draws": 0}
}

player_name = input("Insert player name: ")
print(f"Welcome {player_name}!")
print("Your opponent is RPS-3PO.")
print("Game starts...\n")

while True:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    try:
        player_choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input. Please enter 0, 1, 2, or 3.")
        continue
    
    if player_choice == 0:
        break
    if player_choice not in [1, 2, 3]:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue

    bot_choice = random.randint(1, 3)

    print("\nRock! Paper! Scissors! Shoot!\n")

    print("#" * 25)
    print(f"{player_name} chose {choices[player_choice]}.\n")
    print(ascii_art[player_choice])
    print("#" * 25)
    print(f"RPS-3PO chose {choices[bot_choice]}.\n")
    print(ascii_art[bot_choice])
    print("#" * 25)

    if player_choice == bot_choice:
        print(f"Draw! Both players chose {choices[player_choice]}.\n")
        scores["player"]["draws"] += 1
        scores["bot"]["draws"] += 1
    elif (player_choice == 1 and bot_choice == 3) or \
         (player_choice == 2 and bot_choice == 1) or \
         (player_choice == 3 and bot_choice == 2):
        print(f"{player_name} {choices[player_choice]} beats RPS-3PO {choices[bot_choice]}.\n")
        scores["player"]["wins"] += 1
        scores["bot"]["losses"] += 1
    else:
        print(f"RPS-3PO {choices[bot_choice]} beats {player_name} {choices[player_choice]}.\n")
        scores["player"]["losses"] += 1
        scores["bot"]["wins"] += 1

print("\nResults:")
print(f"{player_name} - wins ({scores['player']['wins']}), losses ({scores['player']['losses']}), draws ({scores['player']['draws']})")
print(f"RPS-3PO - wins ({scores['bot']['wins']}), losses ({scores['bot']['losses']}), draws ({scores['bot']['draws']})")
print("\nProgram ending.")
