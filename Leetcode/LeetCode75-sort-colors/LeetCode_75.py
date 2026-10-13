# LeetCode 75. Sort Colors
nums = [2, 0, 2, 1, 1, 0]

#Brute force
print(sorted(nums))

#Better solution
count_0 = nums.count(0)
count_1 = nums.count(1)
count_2 = nums.count(2)
i = 0
for _ in range(count_0):
    nums[i] = 0
    i += 1
for _ in range(count_1):
    nums[i] = 1
    i += 1
for _ in range(count_2):
    nums[i] = 2
    i += 1
print(nums)

#Optimal solution: Dutch National Flag Algorithm
nums=[2,0,1]
low=0
mid=0
high=len(nums)-1

while mid<=high:
    if nums[mid]==0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low+=1
        mid+=1

    elif nums[mid]==1:
        mid+=1
    
    else:#nums[mid]==2
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1

print(nums)
