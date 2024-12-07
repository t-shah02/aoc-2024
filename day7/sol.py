
def can_compute_expected_value(expected_value: int, number_set: list[int], current_result: int, index: int = 0, concat_enabled: bool = False):
    if index == len(number_set):
        return current_result == expected_value

    # possible operations: +, * and || and go from left-to-right
    new_current_result_mul = number_set[0] if index == 0 else current_result * \
        number_set[index]
    new_current_result_add = number_set[0] if index == 0 else current_result + \
        number_set[index]
    new_current_result_concat = number_set[0] if index == 0 else int(
        str(current_result) + str(number_set[index]))

    if concat_enabled:
        return can_compute_expected_value(expected_value, number_set, new_current_result_mul, index + 1, True) \
            or can_compute_expected_value(expected_value, number_set, new_current_result_add, index + 1, True) \
            or can_compute_expected_value(expected_value, number_set, new_current_result_concat, index + 1, True)

    return can_compute_expected_value(expected_value, number_set, new_current_result_mul, index + 1) or can_compute_expected_value(expected_value, number_set, new_current_result_add, index + 1)


def get_calibration_sum(expected_values: list[int], number_sets: list[list[int]], concat_enabled: bool = False):
    total_calib_sum = 0

    for expected_value, number_set in zip(expected_values, number_sets):
        can_compute_result = can_compute_expected_value(
            expected_value, number_set, 0, 0, concat_enabled)
        if can_compute_result:
            total_calib_sum += expected_value

    return total_calib_sum


def main():
    expected_values: list[int] = []
    number_sets: list[list[int]] = []

    with open('input.txt', 'r') as file:
        for line in file.read().splitlines():
            p1, p2 = line.split(':')
            expected_value = int(p1.strip())
            number_set = [int(x) for x in p2.strip().split(' ')]

            expected_values.append(expected_value)
            number_sets.append(number_set)

    res_part1 = get_calibration_sum(
        expected_values, number_sets, concat_enabled=False)
    print(f'Part 1: {res_part1}')

    res_part2 = get_calibration_sum(
        expected_values, number_sets, concat_enabled=True)
    print(f'Part 2: {res_part2}')


if __name__ == "__main__":
    main()
