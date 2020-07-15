print("welcome")

player_1 = input("Player 1 Name: ")
player_2 = input("Player 2 Name: ")

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
    player_1_num = valid_num(player_1)
    current_sum += player_1_num
    print("Current sum: ", current_sum, " Limit value: ", limit_value)
    if current_sum >= limit_value:
        print(player_2, " wins")
        break
    player_2_num = valid_num(player_2)
    current_sum += player_2_num
    print("Current sum: ", current_sum, " Limit value: ", limit_value)
    if current_sum >= limit_value:
        print(player_1, " wins")
        break