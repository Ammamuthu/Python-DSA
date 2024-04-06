# Basic Of Stack using a List Function
stack=[]
stack.append(10)
stack.append(20)
stack.append(50)
print(stack)
stack.pop()
print(stack)
print(len(stack) == 0)
print(stack[-1])

# Ex : 1
container=[]
def pushed():
    if (len(container) == size_of_cont):
        print("Your alloocated Size is Enough ")
    else :
        usr=int(input("Enter the Element That you want to Add : "))
        container.append(usr)
        print(container)

def poped():
    if (len(container)==0):
        print("Nothing to delete")
    else:
        container.pop()
        print(container)
size_of_cont = int(input("Enter the Size of the Container you want"))
while True:
    human =int(input("Press 1 for add A element 2 for Delete a Element 3 for Quit "))
    if (human ==1):
        pushed()
    elif (human == 2):
        poped()
    elif(human==3):
        break
print("End of the Container......These are the Values inside that")
print(container)

# Using module(Class) Collection to implement stack

import collections
stack = collections.deque()
stack.append(100)
stack.append(200)
print(stack)
stack.pop()
print(stack)

# Implemention of Stack using Module called Queue

from queue import LifoQueue as lq

stack=lq(3)          # -------> We can also Implement our stack size
print(lq)
stack.put(100)
stack.put(22222)
print(stack)
stack.get(timeout=1)
