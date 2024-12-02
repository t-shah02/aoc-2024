def is_report_safe(report: list[int]) -> bool:
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(report)):
        if report[i] < report[i-1]:
            is_increasing = False
            break

    if not is_increasing:
        for i in range(1, len(report)):
            if report[i] > report[i-1]:
                is_decreasing = False
                break

    if not is_increasing and not is_decreasing:
        return False

    for i in range(1, len(report)):
        level_diff = abs(report[i] - report[i-1])
        if level_diff not in range(1, 4):
            return False

    return True


def split_reports(reports: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    safe_reports: list[list[int]] = []
    unsafe_reports: list[list[int]] = []

    for report in reports:
        if is_report_safe(report):
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)

    return safe_reports, unsafe_reports


def part_2(bad_reports: list[list[int]]) -> int:
    total_reformed_reports = 0

    for report in bad_reports:  
        for i in range(len(report)):
            spliced_report = report[:i] + report[i+1:]
            if is_report_safe(spliced_report):
                total_reformed_reports += 1
                break

    return total_reformed_reports


def main():
    reports: list[list[int]] = []

    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            report = [int(val) for val in line.split(' ')]
            reports.append(report)

    safe_reports, unsafe_reports = split_reports(reports)

    res_part1 = len(safe_reports)
    print(f'Part 1: {res_part1}')

    res_part2 = res_part1 + part_2(unsafe_reports)
    print(f'Part 2: {res_part2}')


if __name__ == "__main__":
    main()
