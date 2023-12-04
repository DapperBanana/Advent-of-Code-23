file_name = "C:\\Users\\Austin.Howard\\Downloads\\input.txt"
file = open(file_name, 'r')
file_lines = file.readlines()

#Part 1, let's gooooo
sum_of_all = 0
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
                    if int(amount) > max_red:
                        overflow_flag = True
                case "green":
                    if int(amount) > max_green:
                        overflow_flag = True
                case "blue":
                    if int(amount) > max_blue:
                        overflow_flag = True
    
    if not overflow_flag:
        sum_of_all += int(game_id)

print("Advent of Code Day 2 part 1 answer: " + str(sum_of_all))

#Part 2 bb
sum_of_all = 0

for game in file_lines:

    game_power = 0
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
                    if int(amount) > red_value:
                        red_value = int(amount)
                case "green":
                    if int(amount) > green_value:
                        green_value = int(amount)
                case "blue":
                    if int(amount) > blue_value:
                        blue_value = int(amount)

    game_power = red_value * green_value * blue_value
    sum_of_all += game_power

print("Advent of Code Day 2 part 2 answer: " + str(sum_of_all))
