
OP_PREFIX = 'mul'
ENABLED_PREFIX = 'do'
DISABLED_PREFIX = 'don\'t'


def part_1(contents: str) -> int:
    mul_sum = 0
    bracket_index_stack: list[int] = []

    for i in range(len(contents)):
        if contents[i] == '(':
            bracket_index_stack.append(i)
        elif contents[i] == ')':
            if len(bracket_index_stack) > 0:
                last_open_index = bracket_index_stack.pop()
                part = contents[last_open_index -
                                len(OP_PREFIX): last_open_index] + contents[last_open_index: i + 1]
                if part.startswith(OP_PREFIX):
                    inner_part = contents[last_open_index + 1: i]
                    nums = inner_part.split(',')
                    if len(nums) == 2 and all(x.isnumeric() for x in nums):
                        mul_sum += (int(nums[0]) * int(nums[1]))

    return mul_sum


def part_2(contents: str) -> int:
    mul_sum = 0
    op_enabled = True
    bracket_index_stack: list[int] = []

    for i in range(len(contents)):
        if contents[i] == '(':
            bracket_index_stack.append(i)
        elif contents[i] == ')':
            if len(bracket_index_stack) > 0:
                last_open_index = bracket_index_stack.pop()
                mul_part = contents[last_open_index -
                                    len(OP_PREFIX): last_open_index] + contents[last_open_index: i + 1]
                do_part = contents[last_open_index -
                                   len(ENABLED_PREFIX): last_open_index] + contents[last_open_index: i + 1]
                dont_part = contents[last_open_index -
                                     len(DISABLED_PREFIX): last_open_index] + contents[last_open_index: i + 1]

                if do_part.startswith(ENABLED_PREFIX):
                    op_enabled = True
                elif dont_part.startswith(DISABLED_PREFIX):
                    op_enabled = False
                elif mul_part.startswith(OP_PREFIX):
                    inner_part = contents[last_open_index + 1: i]
                    nums = inner_part.split(',')
                    if len(nums) == 2 and all(x.isnumeric() for x in nums) and op_enabled:
                        mul_sum += (int(nums[0]) * int(nums[1]))

    return mul_sum


def main():
    contents = ""
    with open('input.txt', 'r') as file:
        contents = file.read()

    res_part1 = part_1(contents)
    print(f'Part 1: {res_part1}')

    res_part2 = part_2(contents)
    print(f'Part 2: {res_part2}')


if __name__ == "__main__":
    main()
