

def binary_search(numbers, target, left, right):
    # I keep narrowing the part of the list where the target could be.
    while left <= right:
        middle = left + (right - left) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            # Everything up to the middle is too small.
            left = middle + 1
        else:
            # Everything from the middle onward is too big.
            right = middle - 1

    # The search range is empty, so the target is not in the list.
    return -1


def prepare_set(values):
    # I sort once so I can use binary search for each later lookup.
    # Sorting is preprocessing; it is not part of the O(log n) lookup.
    return sorted(values)


def contains(sorted_values, target):
    # Binary search gives me an index, but this problem only needs yes or no.
    return binary_search(sorted_values, target, 0, len(sorted_values) - 1) != -1


def exponential_search(numbers, target):
    """Search an ascending list, returning an index or -1 if absent."""
    if not numbers:
        return -1

    # I check the first item separately before starting the doubling steps.
    if numbers[0] == target:
        return 0
    if numbers[0] > target:
        return -1

    bound = 1
    # I check positions 1, 2, 4, 8, ... until I reach or pass the target.
    # Checking the length first keeps me from reading past the list.
    while bound < len(numbers) and numbers[bound] < target:
        bound *= 2

    # The last smaller position was bound // 2, so I start after it.
    # I also cap the upper end at the last valid index.
    left = bound // 2 + 1
    right = min(bound, len(numbers) - 1)
    return binary_search(numbers, target, left, right)


if __name__ == "__main__":
    values = [19, 3, 42, 7, 12, 1]
    prepared = prepare_set(values)
    print("Problem 1:")
    for target in [7, 8]:
        print(f"Is {target} in the set? {contains(prepared, target)}")

    numbers = list(range(1, 101))
    print("\nProblem 2:")
    for target in [3, 101]:
        print(f"Index of {target}: {exponential_search(numbers, target)}")