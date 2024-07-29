import random

def generate_crossword(words):
    # Create an empty grid
    grid_size = 10
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Place words horizontally and vertically
    for word in words:
        if random.choice([True, False]):  # Place horizontally
            place_word_horizontal(grid, word)
        else:  # Place vertically
            place_word_vertical(grid, word)

    # Fill in the remaining empty spaces with random letters
    fill_empty_spaces(grid)

    return grid

def place_word_horizontal(grid, word):
    row = random.randint(0, len(grid) - 1)
    col = random.randint(0, len(grid) - len(word))

    for i in range(len(word)):
        grid[row][col + i] = word[i]

def place_word_vertical(grid, word):
    row = random.randint(0, len(grid) - len(word))
    col = random.randint(0, len(grid) - 1)

    for i in range(len(word)):
        grid[row + i][col] = word[i]

def fill_empty_spaces(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def print_crossword(grid):
    for row in grid:
        print(' '.join(row))

# Example usage
word_list = ["PYTHON", "JAVA", "CROSSWORD", "CODE", "COMPUTER"]
crossword_grid = generate_crossword(word_list)

print("Crossword Puzzle:")
print_crossword(crossword_grid)
