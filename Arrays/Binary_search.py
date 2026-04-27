n=[1,2,3,4,5,6,7,8,9,10]
k=10
low=0
high=len(n)-1
while low<=high:
    mid=(low+high)//2
    if n[mid]==k:
        print(mid)
        break
    elif n[mid]<k:
        low=mid+1
    else:
        high=mid-1
else:
    print("Element not found")