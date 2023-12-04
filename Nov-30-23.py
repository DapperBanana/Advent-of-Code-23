
sum_of_all = 0
file_name = "C:\\Users\\Austin.Howard\\Downloads\\input.txt"
file = open(file_name, 'r')
file_lines = file.readlines()

max_red = 12
max_green = 13
max_blue = 14

for game in file_lines:

    overflow_flag = False

    red_value = 0
    green_value = 0
    blue_value = 0

    game_info = game.split(":")
    game_id = game_info[0].split(" ")[1]


    for draws in game_info[1].split(";"):
        for values in draws.split(","):
            amount, color = values.split()
            match color:
                case "red":
                    #red_value += int(amount)
                    if int(amount) > max_red:
                        overflow_flag = True
                case "green":
                    #green_value += int(amount)
                    if int(amount) > max_green:
                        overflow_flag = True
                case "blue":
                    #blue_value += int(amount)
                    if int(amount) > max_blue:
                        overflow_flag = True
    
    #if (red_value > max_red) or (green_value > max_green) or (blue_value > max_blue):
    #    overflow_flag = True
    
    if overflow_flag:
        print(game_id + ": Game invalid")
    else:
        print(game_id + ": Game valid!")
        sum_of_all += int(game_id)

print("Advent of Code Day 2 answer: " + str(sum_of_all))
