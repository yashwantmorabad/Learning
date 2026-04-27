#merge two sorted arrays
n1=[1,2,3,4,5,7,9]
n2=[2,4,6,8,10]
n=[]
i,j=0,0
while i<len(n1) and j<len(n2):
    if n1[i]<n2[j]:
        n.append(n1[i])
        i+=1
    else:
        n.append(n2[j])
        j+=1
if i<len(n1):
    n.extend(n1[i:])
if j<len(n2):
    n.extend(n2[j:])
print(n)

#merge two sorted arrays without duplicates and 
#output array should be sorted
def merge_sorted_arrays(arr1, arr2):
    result = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:  # equal — take one, skip both
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result

# Test
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 3, 6, 7, 10]
print(merge_sorted_arrays(arr1, arr2))