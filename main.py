print("welcome")

player_1 = input("Player 1 Name: ")
player_2 = input("Player 2 Name: ")

limit_value = 10
current_sum = 0

for i in range(limit_value):
    player_1_num = int(input(player_1 + ": "))
    current_sum += player_1_num
    print("Current sum: ", current_sum)
    if current_sum >= limit_value:
        print(player_2, " wins")
        break
    player_2_num = int(input(player_2 + ": "))
    current_sum += player_2_num
    print("Current sum: ",current_sum)
    if current_sum >= limit_value:
        print(player_1, " wins")
        break