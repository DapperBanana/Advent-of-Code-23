import re
re_pattern = r'[!@#$%^&*(),?":{}|<>+=\/-]'
sum_of_all = 0
file_name = "C:\\Users\\Austin.Howard\\Downloads\\input.txt"
file = open(file_name, 'r')
file_lines = file.readlines()
number_list = []
line_length = 0
line_amount = len(file_lines)
for line_index, line in enumerate(file_lines):
    line_length = len(line)
    temp_num = ''
    for char_index, char in enumerate(line):
        if char.isdigit():
            temp_num = temp_num + char
        elif temp_num != '':
            temp_list = [temp_num, line_index, char_index-(len(temp_num))]
            number_list.append(temp_list)
            temp_num = ''

#now that we have the numbers let's go back through and see which values are valid
for number_info in number_list:
    value = number_info[0]
    line_index = number_info[1]
    char_index = number_info[2]

    min_line_index = line_index
    max_line_index = line_index
    min_char_index = char_index
    max_char_index = char_index + (len(value) -1)

    if min_line_index > 0:
        min_line_index -= 1
    if max_line_index < line_amount:
        max_line_index += 1
    if min_char_index > 0:
        min_char_index -= 1
    if max_char_index < line_length:
        max_char_index += 1

    num_is_valid = False

    for search_line_index in range(min_line_index, max_line_index + 1):
        for search_char_index in range(min_char_index, max_char_index + 1):
            for tli, l in enumerate(file_lines):
                if tli == search_line_index:
                    for tci, c in enumerate(l):
                        if tci == search_char_index:
                            result = bool(re.match(re_pattern, c))
                            if result:
                                print(value + " is valid")
                                print("character match: " + c + " || line_index: " + str(search_line_index) + " || char_index: " + str(search_char_index))
                                num_is_valid = True
    
    if num_is_valid:
        sum_of_all += int(value)
    else:
        print(value + " is not valid")
    
    print("-------")

print("Advent of Code Day 3 part 1 answer: " + str(sum_of_all))
