def target_triplet(arr, target):
    # assuming that the given array is sorted
    # else have to do arr.sort()

    result_array = []

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            if arr[i] + arr[left] + arr[right] == target:
                print(
                    "Target location is : ", arr[i], ", ", arr[left], ", ", arr[right]
                )
                # return True  # if we need to return only one such combination
                result_array.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif arr[i] + arr[left] + arr[right] < target:
                left += 1
            elif arr[i] + arr[left] + arr[right] > target:
                right -= 1

    if len(result_array) == 0:
        print("No Match")
    else:
        print(result_array)


target_triplet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
