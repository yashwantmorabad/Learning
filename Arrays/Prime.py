#Factors
#Bruteforce solution
# n=int(input("Enter a number:"))
# Result=[]
# for i in range(1,n+1): #TC O(n)
#       if n%i==0:
#            Result.append(i) #TC O(1)
# print(Result)

#Better solution   
# n=int(input("Enter a number:"))
# Result=[]
# for i in range(1,n//2+1): #TC O(n/2) ~O(n)
#       if n%i==0:
#            Result.append(i) #TC O(1)
# Result.append(n)   
# print(Result)

#Optimal solution
# from math import sqrt
# n=int(input("Enter a number:"))
# result=[]
# for i in range(1,int(sqrt(n))+1):
#     if n%i==0:
#         result.append(i)
#         if n%i!=i:
#             result.append(n//i)
# result.sort()
# print(result)