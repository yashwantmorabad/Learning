n=[11,23,-80,34,100]
l=n[0]
for i in n:
    if i>l:
        l=i
print(l)    
print(max(n[0],l)) #instead if if condition we can use max function

 