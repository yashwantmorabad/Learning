#Factorial of number
# def fun(n):
#     if n==0 or n==1:
#         return 1
#     return n*fun(n-1)
# print(fun(4))

#Reverse a array
# n=[1,2,3,4,5,6,7,8]
# def fun(n,left,right):
#     if left>=right:
#         return
#     n[left],n[right]=n[right],n[left]
#     fun(n,left+1,right-1)

# print(fun(n,1,3))
# print(n)

# left=0
# right=len(n)-1
# while left<right:
#     n[left],n[right]=n[right],n[left]
#     left+=1
#     right-=1
# print(n)

#Palindrome
# def is_palindrome(s):
#     n = len(s)
#     left = 0
#     right = n - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False        # stop immediately on mismatch
#         left += 1
#         right -= 1

#     return True                 # only reached if no mismatch found


# s = "ABCBA"
# print(is_palindrome(s))   # True

# s = "ABCDE"
# print(is_palindrome(s))   # False

# def fun(s,left,right):
#     if left>=right:
#         return True
#     if s[left]!=s[right]:
#         return False
#     return fun(s,left+1,right-1)

# s = "ABCBA"
# print(fun(s,0,len(s)-1))   # True

# s = "ABCDE"
# print(fun(s,0,len(s)-1))   # False 

#Fibonacci Number
# def fun(n):    #O(2^n)
#     if n==0:
#         return 0
#     if n==1 or n==2:
#         return 1
#     return fun(n-1)+fun(n-2)
# print(fun(5))
# print(fun(9))
# print(fun(1))
# print(fun(0))
# print(fun(2))

 