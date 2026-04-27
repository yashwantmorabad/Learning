l=[9,8,7,6,5,4,3,2,1,0]  #TC-O(N^2)
n=len(l)
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)