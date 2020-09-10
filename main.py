import random

def input_num(prompt):
    num = input(prompt)
    for i in range(9):
        try:
            num = int(num)
        except ValueError:
            print(f"Not a number: {i+1}/10")
            num = input(prompt)
    try:
        num = int(num)
    except ValueError:
        print(f"Not a number: {10}/10")
        print("Maximum number of error exceeded")
        exit()
    return num

def valid_num(player):
    prompt = player + ": "
    num = input_num(prompt)
    while 0 >= num or num > max_value:
        print("Invalid Number")
        num = input_num(prompt)
    return num


print("welcome")

COLORS = ["\u001b[31;1m", "\u001b[32m", "\u001b[33;1m", "\u001b[34;1m", "\u001b[35m", "\u001b[36m", "\u001b[37m"]

def valid_name(prompt):
    name = input(prompt)
    while name == "":
        name = input(prompt)
    return name

class Player:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

class Game:
    def __init__(self, players, limit, max_entry) -> None:
        self.PLAYERS = players
        self.limit = limit
        self.maxentry = max_entry
    def play(self):
        current_sum = 0
        while current_sum<self.limit:
            for player in self.PLAYERS:
                num = valid_num(player.color + player.name)
                current_sum += num
                print("Current sum: ", current_sum, " Limit value: ", limit_value)
                if current_sum >= limit_value:
                    PLAYERS.remove(player)
                    print("WINNER(S): ", end=" ")
                    for other_player in PLAYERS:
                        print(other_player.name, end=" ")
                    break


n = input_num("No. of Players: ")

PLAYERS = []
for i in range(n):
    PLAYERS.append(Player(valid_name(f"Player {i} Name: "), random.choice(COLORS)))

limit_value = input_num("Limit Value: ")

print("Limit Value is ", limit_value)

max_value = input_num("Max value: ")

print("Max Value is ", max_value)

game = Game(PLAYERS,limit_value, max_value)

while len(game.PLAYERS) != 1:
    game.play()