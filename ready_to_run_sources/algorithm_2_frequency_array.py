def iterative2_frequency_array(arr):
    counts = {}
    limit = len(arr) // 2

    for index, value in enumerate(arr):
        counts[value] = counts.get(value, 0) + 1
        if counts[value] > limit:
            return index

    return -1


def print_array(arr):
    print("[" + ", ".join(str(value) for value in arr) + "]")


def run_case(arr, case_number):
    result = iterative2_frequency_array(arr)
    print(f"Case {case_number}")
    print("Array:", end=" ")
    print_array(arr)

    if result != -1:
        print(f"Result: dominator index = {result}, value = {arr[result]}")
    else:
        print("Result: no dominator")

    print()


if __name__ == "__main__":
    cases = [
        [3, 4, 3, 2, 3, -1, 3, 3],
        [1, 2, 3, 4, 5],
        [2, 2, 2, 2, 1, 3],
    ]

    for case_number, case in enumerate(cases, start=1):
        run_case(case, case_number)
