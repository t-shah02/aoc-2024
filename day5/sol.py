import copy
import functools


def is_correctly_ordered(page_update: list[int], order_map: dict[int, list[int]]) -> bool:
    update_is_good = True

    for i in range(len(page_update)):
        if page_update[i] not in order_map:
            continue

        after_pages = order_map[page_update[i]]
        page_is_good = True

        for after_page in after_pages:
            try:
                after_page_index = page_update.index(after_page)
                if after_page_index < i:
                    page_is_good = False
                    break
            except:
                pass

        if not page_is_good:
            update_is_good = False
            break

    return update_is_good


def reorder_page_update(page_update: list[int], order_map: dict[int, list[int]]):
    def compare_pages(page_number_a: int, page_number_b: int) -> int:
        if page_number_a not in order_map:
            return 0

        after_pages = order_map[page_number_a]
        if page_number_b not in after_pages:
            return 0

        return -1

    page_update_cpy = copy.deepcopy(page_update)
    page_update_cpy.sort(key=functools.cmp_to_key(compare_pages))
    return page_update_cpy


def get_order_map(page_ordering_rules: list[tuple[int, int]]) -> dict[int, list[int]]:
    order_map: dict[int, list[int]] = {}

    for num1, num2 in page_ordering_rules:
        if num1 not in order_map:
            order_map[num1] = []

        order_map[num1].append(num2)

    return order_map


def part_1(page_ordering_rules: list[tuple[int, int]], page_updates: list[list[int]]) -> int:
    middle_page_number_sum = 0
    order_map = get_order_map(page_ordering_rules)

    for page_update in page_updates:
        if is_correctly_ordered(page_update, order_map):
            midpoint = len(page_update) // 2
            middle_page = page_update[midpoint]
            middle_page_number_sum += middle_page

    return middle_page_number_sum


def part_2(page_ordering_rules: list[tuple[int, int]], page_updates: list[list[int]]) -> int:
    middle_page_number_sum = 0
    order_map = get_order_map(page_ordering_rules)

    for page_update in page_updates:
        if not is_correctly_ordered(page_update, order_map):
            ordered_page_update = reorder_page_update(page_update, order_map)
            midpoint = len(page_update) // 2
            middle_page = ordered_page_update[midpoint]
            middle_page_number_sum += middle_page

    return middle_page_number_sum


def main():
    page_ordering_rules: list[tuple[int, int]] = []
    page_updates: list[list[int]] = []

    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        reading_ordering_rules = True

        for line in lines:
            if len(line) == 0:
                reading_ordering_rules = False
                continue

            if reading_ordering_rules:
                parts = line.split('|')
                page_ordering_rules.append((int(parts[0]), int(parts[1])))
            else:
                page_updates.append([int(num) for num in line.split(',')])

    res_part1 = part_1(page_ordering_rules, page_updates)
    print(f'Part 1: {res_part1}')

    res_part2 = part_2(page_ordering_rules, page_updates)
    print(f'Part 2: {res_part2}')


if __name__ == "__main__":
    main()
