def findPeak(arr, n): 
    l = 0
    r = n-1

    while(l <= r):
        mid = (l + r) >> 1

        # first case if mid is the answer
        if((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            break

        # move the right pointer
        if(mid > 0 and arr[mid - 1] > arr[mid]):
            r = mid - 1

        # move the left pointer
        else:
            l = mid + 1

    return mid


# Driver Code
arr = [1,1,1,3,2,1,2]
n = len(arr)
print(f"Index of a peak point is {findPeak(arr, n)}")
