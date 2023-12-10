# Open the text file for reading
file_path = "C:\\Users\\Austin.Howard\\Downloads\\input.txt"
try:
    with open(file_path, "r") as file:
        final_num = 0
        # Loop over each line in the file
        for line in file:
            # Process each line here
            first_digit = None
            last_digit = None
            for char in line:
                if char.isdigit():
                    if first_digit is None:
                        first_digit = int(char)
                        last_digit = int(char)
                    else:
                        last_digit = int(char)
            combined_number = int(str(first_digit) + str(last_digit))
            final_num += combined_number
        print("Advent of Code Day 1 Part 1 answer: " + str(final_num))
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
