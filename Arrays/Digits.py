#Extraction of digits using while
#Time complexity of the code containing
#below while loop is O(log10(N))
#Where 10 is the number is dividing actual number
# n=int(input("Enter a number:"))
# count=0
# while n>0:
#     lastdigit=n%10
#     print(lastdigit)
#     count+=1
#     n=n//10
# print("The number of digits:",count)

#Extraction of digits using log
# from math import * 
# def countdigits(num):
#     print(int(log10(num)+1))

# n=int(input("Enter a number:"))
# countdigits(n)

#Palindrome
# n=int(input("Enter a number:"))
# num=n
# Pal=0
# while n>0:
#     lastdigit=n%10
#     print(lastdigit)
#     Pal=lastdigit+Pal*10
#     n=n//10
# if num==Pal:
#     print("Plaindrome")
# else:
#     print("Not a plaindrome")

#Armstrong Number
# n=(input("Enter a number:"))
# No_of_digits=len(str(n))   
# n=int(n)
# num=n
# total=0   
# while n>0:
#     lastdigit=n%10
#     total=total+lastdigit**No_of_digits
#     n=n//10
# if num==total:
#     print("It is a armstrong number")
# else:
#     print("It is not a armstrong no.") 