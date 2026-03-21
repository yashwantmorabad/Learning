l=[9,8,7,6,5,4,3,2,1,0]  #TC-O(log(base(2))N)
def merge(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<n:
            result.append(right[j])
            j+=1
    return result

def sort_(l):
    if len(l)<=1:
        return l
    mid=len(l)//2
    left_arr=l[:mid]
    right_arr=l[mid:]
    left=sort_(left_arr)
    right=sort_(right_arr)
    return merge(left,right)

print(sort_(l))


