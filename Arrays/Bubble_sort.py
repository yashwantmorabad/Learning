BL=[9,8,7,6,5,4,3,2,1,10]   #TC-O(N^2) Worst case
n=len(BL)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if BL[j]>BL[j+1]:
            BL[j],BL[j+1]=BL[j+1],BL[j]
print(BL)

B=[1,2,3,4,5,6,7,8,9,10]   #TC-O(N) Best case
n=len(B)
for i in range(n-2,-1,-1):
    is_swap=False
    for j in range(0,i+1):
        if B[j]>B[j+1]:
            B[j],B[j+1]=B[j+1],B[j]
            is_swap=True
    if is_swap==False:
        break
print(B)