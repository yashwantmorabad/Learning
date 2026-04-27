#Bruteforce sol
# n=[9,9,8,8,7,7,6,6,5,5]
# m=[1,2,3,4,5,6,7,8,9,10]
# for i in m:
#     count=0
#     for x in n:  #TC O(m*n)
#         if x==i:
#             count+=1
#     print(count)


# n=[9,9,8,8,7,7,6,6,5,5]
# m=[0,1,2,3,4,5,6,7,8,9]
# hash_list=[0]*10
# for i in n:
#     hash_list[i]+=1

# for i in m:            #TC O(m+n)
#       if i<0 or i>9:
#         print(0)
#       else:
#         print(hash_list[i])

# n=[9,9,8,8,7,7,6,6,5,5]
# m=[0,1,2,3,4,5,6,7,8,9]
# Di={}
# for i in n:
#     Di[i]=Di.get(i,0)+1
# for i in m:
#     if i<0 or i>9:
#         print(0)
#     else:
#         print(Di.get(i,0))

#character Hashing
#Bruteforce sol
s="ababcdcede"
q=["a","b","c","d","e"]
# for i in q:
#     count=0
#     for j in s:
#         if i==j:
#             count+=1
#     print(count)

#Better sol
hash_list=[0]*27
for ch in s:
     asci_val=ord(ch)
     index=asci_val-97
     hash_list[index]+=1

for ch in q:
     asci_val=ord(ch)
     index=asci_val-97
     print(hash_list[index])