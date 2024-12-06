with open("input.txt") as f:
    lines = f.readlines()

def part_one():
    split_lines = [line.split() for line in lines]
    reports = [[int(num) for num in line] for line in split_lines]
    are_reports_safe = [is_safe(report) for report in reports]
    safe_reports = [r for r in are_reports_safe if r]

    print(len(safe_reports))

def part_two():
    split_lines = [line.split() for line in lines]
    reports = [[int(num) for num in line] for line in split_lines]
    are_reports_safe = [is_any_combo_safe(report) for report in reports]
    safe_reports = [r for r in are_reports_safe if r]

    print(len(safe_reports))

def is_safe(report):
    decreasing = report[0] > report[1]
    for i in range(0, len(report)-1):
        this_decreased = report[i] > report[i+1]
        if decreasing != this_decreased:
            return False

        diff = abs(report[i] - report[i+1])
        if diff < 1:
            return False
        if diff > 3:
            return False
    return True

def is_any_combo_safe(report):
    for i in range(0, len(report)):
        report_copy = [r for r in report]
        del report_copy[i]
        if is_safe(report_copy):
            return True
    return False

part_one()
part_two()


