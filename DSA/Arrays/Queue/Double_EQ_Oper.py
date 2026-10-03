from collections import deque
dq = deque([10, 20, 30, 40, 50])

"Rotate 1 step to the right (50 moves to the front)"
dq.rotate(2)
print(dq) 

"Rotate 2 steps to the left"
dq.rotate(-2)
print(dq)  

"Add to right"
dq.extend([60,60])
print(dq)  

"Add to left"
dq.extendleft([5,1])
print(dq)  

"Occurance"
print(dq.count(60))

"Remove"
dq.remove(1)
print(dq)  

"Clear"
dq.clear()
print(dq)  