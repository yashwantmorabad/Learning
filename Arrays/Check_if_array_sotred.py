#Check if array is sorted or not
#Bruteforce solution
# n=[1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]>n[j]:
#             print("False")
#             break
#         else:
#             print("True")
#         break

#Optimal solution
n=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(n)-1):
    if n[i]>n[i+1]:
        print("False")
        break
    else:
        print("True")
    break