#Brute Force Approach
n=[1,2,3,4,5,6,7,8,9,10]
k=1
for i in range(0,k):
    temp=n[len(n)-1]
    for j in range(len(n)-1,-1,-1):
        n[j]=n[j-1]
    n[0]=temp
print(n)
#Optimal Approach
n=[1,2,3,4,5,6,7,8,9,10]
k=2
n=n[len(n)-k:]+n[:len(n)-k]
print(n)