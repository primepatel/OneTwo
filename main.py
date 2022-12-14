import random

print("welcome")

COLORS = ["\u001b[31;1m", "\u001b[32m", "\u001b[33;1m", "\u001b[34;1m", "\u001b[35m", "\u001b[36m", "\u001b[37m"]

def valid_name(prompt):
    name = input(prompt)
    while name == "":
        name = input(prompt)
    return name


player_1 = valid_name("Player 1 Name: ")
player_2 = valid_name("Player 2 Name: ")

for i in range(10):
    if player_1 == player_2:
        print(f"Same Name: {i+1}/10")
        print("Choose different name")
        player_2 = valid_name("Player 2 Name: ")
    else:
        break

if player_1 == player_2:
    print("Reach maximum error limit")
    exit()

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

limit_value = input_num("Limit Value: ")

print("Limit Value is ", limit_value)

max_value = input_num("Max value: ")

print("Max Value is ", max_value)

def valid_num(player):
    prompt = player + ": "
    num = input_num(prompt)
    while 0 >= num or num > max_value:
        print("Invalid Number")
        num = input_num(prompt)
    return num

current_sum = 0

for i in range(limit_value):
    player_1_num = valid_num(COLORS[random.randint(0, 6)] + player_1)
    current_sum += player_1_num
    print("Current sum: ", current_sum, " Limit value: ", limit_value)
    if current_sum >= limit_value:
        print(player_2, " wins")
        break
    player_2_num = valid_num(COLORS[random.randint(0, 6)] + player_2)
    current_sum += player_2_num
    print("Current sum: ", current_sum, " Limit value: ", limit_value)
    if current_sum >= limit_value:
        print(player_1, " wins")
        break