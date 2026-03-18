D={}
nums=[1,2,3,4,4,5,4,5,6,4,3,2,1]
for i in range(0,len(nums)):
    if nums[i] in D:
        D[nums[i]]+=1
    else:
        D[nums[i]]=1    
print(D)
