def count_xmas_occurrences(grid):
    # Helper function to extract diagonals
    def get_diagonals(grid):
        diagonals = []
        rows, cols = len(grid), len(grid[0])

        # Top-left to bottom-right diagonals
        for start in range(-(rows - 1), cols):
            diagonal = []
            for r in range(rows):
                c = start + r
                if 0 <= c < cols:
                    diagonal.append(grid[r][c])
            diagonals.append(''.join(diagonal))

        # Top-right to bottom-left diagonals
        for start in range(rows + cols - 1):
            diagonal = []
            for r in range(rows):
                c = start - r
                if 0 <= c < cols:
                    diagonal.append(grid[r][c])
            diagonals.append(''.join(diagonal))

        return diagonals

    # Helper function to count occurrences in a single line
    def count_in_line(line, word):
        count = 0
        len_word = len(word)
        for i in range(len(line) - len_word + 1):
            if line[i:i + len_word] == word:
                count += 1
        return count

    word = "XMAS"
    reversed_word = word[::-1]
    total_count = 0

    # Count in rows
    for row in grid:
        line = ''.join(row)
        total_count += count_in_line(line, word)
        total_count += count_in_line(line, reversed_word)

    # Count in columns
    for col in zip(*grid):
        line = ''.join(col)
        total_count += count_in_line(line, word)
        total_count += count_in_line(line, reversed_word)

    # Count in diagonals
    diagonals = get_diagonals(grid)
    for diagonal in diagonals:
        total_count += count_in_line(diagonal, word)
        total_count += count_in_line(diagonal, reversed_word)

    return total_count

# Example word search grid
grid = [
    list("MMMSXXMASM"),
    list("MSAMXMSMSA"),
    list("AMXSXMAAMM"),
    list("MSAMASMSMX"),
    list("XMASAMXAMM"),
    list("XXAMMXXAMA"),
    list("SMSMSASXSS"),
    list("SAXAMASAAA"),
    list("MAMMMXMMMM"),
    list("MXMXAXMASX")
]

# Count occurrences
result = count_xmas_occurrences(grid)
print("Total occurrences of 'XMAS':", result)
