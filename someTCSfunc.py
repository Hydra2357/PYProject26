def first_non_repeating(s):
    if not s:
        return "-1"
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] == 1:
            return char
    return "-1"


def find_equilibrium_index(arr):
    if not arr:
        return -1
    total = sum(arr)
    left = 0
    for i in range(len(arr)):
        if left == total - left - arr[i]:
            return i
        left += arr[i]
    return -1


def first_and_last_position(arr, target):
    if not arr:
        return (-1, -1)

    # Find first occurrence
    left, right = 0, len(arr) - 1
    first = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if first == -1:
        return (-1, -1)

    # Find last occurrence
    left, right = 0, len(arr) - 1
    last = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return (first, last)


def majority_element(arr):
    if not arr:
        return -1

    # Boyer-Moore Voting
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Verify
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1


# ────────────────────────────────────────────────
#                  MAIN PROGRAM
# ────────────────────────────────────────────────

while True:
    print("\n" + "="*50)
    print("   Choose a problem (1-4) or 0 to exit")
    print("1. First Non-Repeating Character")
    print("2. Equilibrium Index (Pivot Index)")
    print("3. First and Last Occurrence of Target")
    print("4. Majority Element (> n/2 times)")
    print("0. Exit")
    print("="*50)

    try:
        choice = int(input("Enter your choice (0-4): ").strip())
    except:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 0:
        print("\nThank you! Goodbye.")
        break

    elif choice == 1:
        s = input("Enter the string: ").strip()
        result = first_non_repeating(s)
        print(f"First non-repeating character  →  {result}")

    elif choice == 2:
        try:
            arr = list(map(int, input("Enter array (space separated): ").split()))
            idx = find_equilibrium_index(arr)
            print(f"Equilibrium index             →  {idx}")
        except:
            print("Invalid input. Please enter numbers only.")

    elif choice == 3:
        try:
            arr = list(map(int, input("Enter sorted array (space separated): ").split()))
            target = int(input("Enter target value: "))
            first, last = first_and_last_position(arr, target)
            print(f"First and last occurrence     →  ({first}, {last})")
        except:
            print("Invalid input.")

    elif choice == 4:
        try:
            arr = list(map(int, input("Enter array (space separated): ").split()))
            ans = majority_element(arr)
            print(f"Majority element              →  {ans}")
        except:
            print("Invalid input. Please enter numbers only.")

    else:
        print("Please choose a valid option (0-4)")