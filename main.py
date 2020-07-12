print("welcome")

player_1 = input("Player 1 Name: ")
player_2 = input("Player 2 Name: ")

limit_value = int(input("Limit Value: "))
max_value = int(input("Max value: "))

def valid_num(player):
    num = int(input(player + ": "))
    while 0 >= num or num > max_value:
        print("Invalid Number")
        num = int(input(player + ": "))
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