#Search in rotated array
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        # Left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1     # target is in the sorted left half
            else:
                lo = mid + 1     # target is in the right half
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1     # target is in the sorted right half
            else:
                hi = mid - 1     # target is in the left half
    return -1

a=[4, 5, 6, 7, 0, 1, 2]
print(search_rotated(a,0))