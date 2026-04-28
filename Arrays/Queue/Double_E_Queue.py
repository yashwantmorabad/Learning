from collections import deque

dq = deque()

# Insert at Rear (Normal Enqueue)
dq.append(10)
dq.append(20)

# Insert at Front (Specific to Deque)
dq.appendleft(5)
print("After insertions:", dq)  
dq.append(30)
print("After insertions:", dq) 

# Delete from Front (Normal Dequeue)
dq.popleft()

# Delete from Rear (Specific to Deque)
dq.pop()
print("After deletions:", dq) 