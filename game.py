import random
from enum import Enum
from colorama import Fore, Style, init

init(autoreset=True)

def find_approximate_value(value, percent_range):
    lowest = value - (percent_range / 100) * value
    highest = value + (percent_range / 100) * value
    return random.randint(int(lowest), int(highest))

class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0

    def add_gold(self, amount):
        self.gold = max(0, self.gold + amount)

def draw_event():
    event = random.choices(event_list, event_probabilities)[0]
    return event

def draw_chest():
    color = random.choices(chest_colors_list, chest_colors_probabilities)[0]
    reward = find_approximate_value(reward_for_chest[color], 10)
    color_text = {
        Colors.Green: Fore.GREEN,
        Colors.Orange: Fore.YELLOW,
        Colors.Purple: Fore.MAGENTA,
        Colors.Gold: Fore.LIGHTYELLOW_EX
    }
    print(color_text[color] + f"The chest color is {color.value}!")
    return color, reward

def draw_trap():
    print(Fore.RED + "Oh no! You fell into a trap and lost 500 gold!")
    return -500

def play_game(player, turns):
    print(f"Welcome to the game, {player.name}!")
    print(f"You have {turns} turns to play. See how much gold you can acquire!")
    print("Move forward by answering 'yes' or 'y'.\n")

    for turn in range(1, turns + 1):
        answer = input(f"Turn {turn}: Do you want to move forward? (yes/y): ").lower()
        if answer in ("yes", "y"):
            print("Great, let's see what you got...")
            event = draw_event()
            if event == Event.Chest:
                print("You've found a CHEST!")
                color, reward = draw_chest()
                print(f"You've acquired {reward} gold pieces!")
                player.add_gold(reward)
            elif event == Event.Trap:
                loss = draw_trap()
                player.add_gold(loss)
            else:
                print("Nothing here, just an empty space.")
        elif answer in ("no", "n"):
            print("You decided to stop playing, goodbye!")
            break
        else:
            print("Invalid command. Please type 'yes', 'y', 'no', or 'n'.")
    print(f"\nCongratulations, {player.name}! You have acquired {player.gold} gold pieces in total!")

Event = Enum('Event', ['Chest', 'Empty', 'Trap'])
event_dictionary = {
    Event.Chest: 0.5,
    Event.Empty: 0.4,
    Event.Trap: 0.1
}
event_list = tuple(event_dictionary.keys())
event_probabilities = tuple(event_dictionary.values())

Colors = Enum('Colors', {
    'Green': 'zielony',
    'Orange': 'pomaranczowy',
    'Purple': 'fioletowy',
    'Gold': 'zloty'
})
chest_colors_dictionary = {
    Colors.Green: 0.75,
    Colors.Orange: 0.2,
    Colors.Purple: 0.04,
    Colors.Gold: 0.01
}
chest_colors_list = tuple(chest_colors_dictionary.keys())
chest_colors_probabilities = tuple(chest_colors_dictionary.values())

reward_for_chest = {
    chest_colors_list[i]: (i + 1) * (i + 1) * 1000
    for i in range(len(chest_colors_list))
}

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    player = Player(player_name)
    play_game(player, turns=5)