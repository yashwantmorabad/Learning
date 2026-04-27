n=[1,2,10,3,4,5,6,7,8,9,10]
k=10
for i in range(0,len(n)):
    if n[i]==k:
        print(i) 
        break
else:
    print("Element not found")
        
        