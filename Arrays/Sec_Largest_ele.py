#Brute force solution
#Sol-sort the array and print the n-2 element
#If sorting is not allowed
#Better sloution
n=[1,2,3,4,5,6,7,8,9,10]
largest=float('-inf')
second_largest=float('-inf')
for i in range(0,len(n)):
    largest=max(largest,n[i])
for i in range(0,len(n)):
    if n[i]>second_largest and n[i]!=largest:
        second_largest=n[i]
print(second_largest)       
#optimal solution 
n=[1,2,3,4,5,6,7,8,9,10]
largest=float('-inf')
second_largest=float('-inf')
for i in n:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print(second_largest)