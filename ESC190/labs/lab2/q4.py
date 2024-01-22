def binary_search_deluxe(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid > num):
            left = mid + 1
        elif (mid < num):
            right = mid - 1
        else:
            #found one of the elements at index mid
            left = mid - 1
            right = mid + 1
            while (left > -1 and arr[left] == num):
                left -= 1
            while (right < len(arr) and arr[right] == num):
                right += 1

            print([left + 1, right + 1])

            
binary_search_deluxe([1, 2, 3, 10, 10, 10, 12, 12], 10)
