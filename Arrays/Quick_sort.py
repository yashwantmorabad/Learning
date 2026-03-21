#Pick a pivot i.e element in the list or array
#Put pivpt at it's correct posotion
#Put all small elements in left side and large elements in right side
nums=[4,1,2,3,7,6,8]    #TC-O(n**2)
def partiton(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j

def q_sort(nums,low,high):
    if low<high:
        p_index=partiton(nums,low,high)
        q_sort(nums,low,p_index-1)
        q_sort(nums,p_index+1,high)

print(q_sort(nums,0,len(nums)-1))
print(nums)

#Best case
nums = [4, 1, 2, 3, 7, 6, 8]

def median_of_three(nums, low, high):
    mid = (low + high) // 2
    # Sort low, mid, high positions so median ends up at low
    if nums[low] > nums[mid]:
        nums[low], nums[mid] = nums[mid], nums[low]
    if nums[low] > nums[high]:
        nums[low], nums[high] = nums[high], nums[low]
    if nums[mid] > nums[high]:
        nums[mid], nums[high] = nums[high], nums[mid]
    # Place median at low so partition() picks it as pivot
    nums[low], nums[mid] = nums[mid], nums[low]

def partition(nums, low, high):
    median_of_three(nums, low, high)   # <-- pivot is now the median
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j > low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def q_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        q_sort(nums, low, p_index - 1)
        q_sort(nums, p_index + 1, high)

q_sort(nums, 0, len(nums) - 1)
print(nums)
# Output: [1, 2, 3, 4, 6, 7, 8]

#Average case
import random

nums = [4, 1, 2, 3, 7, 6, 8]

def partition(nums, low, high):
    # Pick random index and swap it to low
    rand_index = random.randint(low, high)
    nums[low], nums[rand_index] = nums[rand_index], nums[low]
    
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j > low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def q_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        q_sort(nums, low, p_index - 1)
        q_sort(nums, p_index + 1, high)

q_sort(nums, 0, len(nums) - 1)
print(nums)
# Output: [1, 2, 3, 4, 6, 7, 8]