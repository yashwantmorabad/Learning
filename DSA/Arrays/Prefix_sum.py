def sum(n):
    a=len(n)
    p=[0]*a
    p[0]=n[0]
    for i in range(1,a):
        p[i]=p[i-1]+n[i]
    return p

l=[1,2,3,4,5,6,7,8,9,10]
print(sum(l))