def dutch_national_flag(arr):
    low = 0          # pointer for next position of 0
    mid = 0          # current element being examined
    high = len(arr) - 1  # pointer for next position of 2

    while mid <= high:
        if arr[mid] == 0:
            # Swap with low and move both pointers
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 13
        elif arr[mid] == 1:
            # Element is in correct position → just move mid
            mid += 1
        else:  # arr[mid] == 2
            # Swap with high and move high only (mid stays)
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

if __name__ == "__main__":
    # Read input
    n = int(input().strip())
    arr = list(map(int, input().split()))

    # Sort using Dutch National Flag
    sorted_arr = dutch_national_flag(arr)
    print(*sorted_arr)