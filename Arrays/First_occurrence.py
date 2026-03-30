def first_occurrence(arr, target):
    lo, hi, ans = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            ans = mid        # record, but keep going left
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans
a=[1,2,2,2,3,4]
print(first_occurrence(a,2))