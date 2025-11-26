def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

test_list_sorted = sorted([3,1,4,1,5,9,2,6,5,3,5])
result = binary_search(test_list_sorted, 6)
print(f"Binary search: Index of 6 in sorted list is {result}")