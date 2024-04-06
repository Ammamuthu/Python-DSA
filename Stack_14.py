stack=[1,2,3,4,5]

print(type(stack))

# acessing
print(stack[-1])  #It print the last elememt

#append
stack.append(6)
print(stack)

#delete
stack.pop()
print(stack)

#searching
ans=3
if ans in stack:
    print(True)

# =====================================================================

from collections import deque

arr = deque([7,5,3,2,1])

print(type(arr))


print(arr)

arr.append(0)
print(arr)
arr.appendleft(9)

print(arr)

arr.pop()
print(arr)
arr.popleft()
print(arr)
