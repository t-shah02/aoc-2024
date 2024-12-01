from collections import Counter


def part_1(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    distance = 0

    for n1, n2 in zip(left, right):
        distance += abs(n1 - n2)

    return distance


def part_2(left: list[int], right: list[int]) -> int:
    similarity_score = 0
    right_counts = Counter(right)

    for n in left:
        n_count = right_counts[n]
        similarity_score += (n * n_count)

    return similarity_score


def main():
    left: list[int] = []
    right: list[int] = []

    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            n1, n2 = [int(x) for x in line.split(" ") if len(x) > 0]
            left.append(n1)
            right.append(n2)

    res_part1 = part_1(left, right)
    print(f'Part 1: {res_part1}')

    res_part2 = part_2(left, right)
    print(f'Part 2: {res_part2}')


if __name__ == "__main__":
    main()
