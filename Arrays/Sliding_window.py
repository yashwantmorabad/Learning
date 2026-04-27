def sliding_window(arr, k):
    left = 0
    current_sum = 0
    max_sum = float('-inf')

    for right in range(len(arr)):
        current_sum += arr[right]          # Expand
        if right - left + 1 > k:           # Shrink to keep size = k
            current_sum -= arr[left]
            left += 1
        max_sum = max(max_sum, current_sum)
    return max_sum

a=[2,1,5,1,3,2]
k=3
print(sliding_window(a,k))