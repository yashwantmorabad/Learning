#Selection sort
n=[7,8,5,6,3,2,1,4,9,10]
def selection_sort(n):
    for i in range(0,len(n)):
        min_ind=i
        for j in range(i+1,len(n)):
            if n[j]<n[min_ind]:
                min_ind=j
        n[i],n[min_ind]=n[min_ind],n[i]
    return n
            
print(selection_sort(n))

n=[7,8,5,6,3,2,1,4,9,10]
def selection_sort(n):
    for i in range(0,len(n)):
        max_ind=i
        for j in range(i+1,len(n)):
            if n[j]>n[max_ind]:
                max_ind=j
        n[i],n[max_ind]=n[max_ind],n[i]
    return n
            
print(selection_sort(n))