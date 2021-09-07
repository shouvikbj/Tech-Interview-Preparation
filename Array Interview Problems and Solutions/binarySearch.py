# Binary search recursive


def binary_search_helper(arr, val, low, high):
    # handling the corner case
    if low > high:
        return "No Match"

    mid = low + ((high - low) // 2)

    if arr[mid] == val:
        return mid
    elif val < arr[mid]:
        return binary_search_helper(arr, val, low, (mid - 1))
    else:
        return binary_search_helper(arr, val, (mid + 1), high)


def binarySearch_recursive(arr, val):
    result = binary_search_helper(arr, val, 0, (len(arr) - 1))
    return result


actual_arr = [2, 5, 6, 7, 10, 15, 22, 30, 50]
target_val_1 = 15
target_val_2 = 40

print("Index : ", binarySearch_recursive(actual_arr, target_val_1))
print("Index : ", binarySearch_recursive(actual_arr, target_val_2))


# Binary search iterative


def binarySearch_iterative(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == val:
            return mid
        if val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return "No Match"


actual_arr = [2, 5, 6, 7, 10, 15, 22, 30, 50]
target_val_1 = 22
target_val_2 = 45

print("Index : ", binarySearch_iterative(actual_arr, target_val_1))
print("Index : ", binarySearch_iterative(actual_arr, target_val_2))
