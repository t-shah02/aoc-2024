from collections import Counter

SEARCH_WORD_P1 = 'XMAS'
SEARCH_WORD_P2 = 'MAS'


def in_bounds(grid, row, col): return row >= 0 and row < len(
    grid) and col >= 0 and col < len(grid[row])


def search_neighbors(grid: list[list[str]], row: int, col: int, search_word: str) -> int:
    valid_occurences = []

    # check forward
    coords = [(row, col + i) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

    # check backward
    coords = [(row, col - i) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

    # check top
    coords = [(row - i, col) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

    # check bottom
    coords = [(row + i, col) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

    # check diagonal top left
    coords = [(row - i, col - i) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

    # check diagonal top right
    coords = [(row - i, col + i) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

    # check diagonal bottom left
    coords = [(row + i, col - i) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

        # check diagonal bottom right
    coords = [(row + i, col + i) for i in range(len(search_word))]
    if all(in_bounds(grid, r, c) for r, c in coords) and "".join(grid[r][c] for r, c in coords) == search_word:
        valid_occurences.append(coords)

    return valid_occurences


def is_diagonal(coords: list[tuple[int, int]]):
    return coords[0][0] != coords[1][0] and coords[0][1] != coords[1][1]


def part_1(grid: list[list[str]]) -> int:
    total_xmas = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            total_xmas += len(search_neighbors(grid, row, col, SEARCH_WORD_P1))

    return total_xmas


def part_2(grid: list[list[str]]) -> int:
    mas_pairs = []
    diag_coord_counts = Counter()
    total_x_mas = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            coords = search_neighbors(grid, row, col, SEARCH_WORD_P2)
            for coord in coords:
                if is_diagonal(coord):
                    mas_pairs.append(coord)
                    for pair in coord:
                        diag_coord_counts[pair] += 1
                        pair_row, pair_col = pair
                        if diag_coord_counts[pair] > 1 and grid[pair_row][pair_col] == 'A':
                            total_x_mas += 1

    return total_x_mas


def main():
    grid = []
    with open('input.txt', 'r') as file:
        for line in file.read().splitlines():
            grid.append(list(line))

    res_part1 = part_1(grid)
    print(f'Part 1: {res_part1}')

    res_part2 = part_2(grid)
    print(f'Part 2: {res_part2}')


if __name__ == "__main__":
    main()
