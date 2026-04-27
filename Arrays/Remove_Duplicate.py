#Brute Force Approach
# nums=[1,1,2,2,3,3,4,4,5,5]
# n=len(nums)
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i]==nums[j]:
#             print(nums[i])
#             break


#Optimal Approach
nums=[1,1,2,2,2,3,3,4,4,5,5,5,5,5,5]
n=len(nums)
D=[]
for i in range(n):
    if nums[i] in D:
        continue
    else:
        D.append(nums[i])
print(D)