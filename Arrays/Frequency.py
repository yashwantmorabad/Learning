D={}
nums=[1,2,3,4,4,5,4,5,6,4,3,2,1]
for i in range(0,len(nums)):    #TC O(n)
    if nums[i] in D:   #TC O(1)
        D[nums[i]]+=1  #TC O(1)
    else:
        D[nums[i]]=1   #TC O(1)
print(D)

Di={}
nums=[1,2,3,4,4,5,4,5,6,4,3,2,1]
n=len(nums)
for i in range(0,n):
    Di[nums[i]]=Di.get(nums[i],0)+1
print(Di)