def calculate_points(cards):
    total_points = 0

    for card in cards:
        numbers, your_numbers = card.split('|')
        winning_numbers = set(map(int, numbers.split()))
        your_numbers = list(map(int, your_numbers.split()))

        points = 0
        for num in your_numbers:
            if num in winning_numbers:
                points += 1
                winning_numbers.remove(num)
                points *= 2

        total_points += points

    return total_points

def read_cards_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if not line.startswith('Card')]

file_path = "C:\\Users\\Austin.Howard\\Downloads\\input.txt"
cards_input = read_cards_from_file(file_path)
total_points = calculate_points(cards_input)

print(f"The Elf's pile of scratchcards is worth {total_points} points.")
