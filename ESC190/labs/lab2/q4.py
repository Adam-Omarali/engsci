def binary_search_deluxe(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if (arr[mid] > num):
            left = mid + 1
        elif (arr[mid] < num):
            right = mid - 1
        else:
            #found one of the elements at index mid
            left = mid - 1
            right = mid + 1
            while (left > -1 and arr[left] == num):
                left -= 1
            while (right < len(arr) and arr[right] == num):
                right += 1

            return [left + 1, right - 1]

            
print(binary_search_deluxe([1, 2, 3, 10, 10, 10, 10, 12, 12], 10))
