# implmenting using a Modules/classes
import collections
q=collections.deque()

q.append(10)
q.append(20)
q.append(30)
print(q)
q.popleft() #--------it will del first elemnt FIFO 
print(q)

# ----or----------

q.appendleft(100)
q.appendleft(200)
q.appendleft(300)
print(q)
q.pop() #----------for queue--------> This way We can also use 



# ==================================================================================================

import queue
que=queue.Queue(3)    #--------->If i give empty it will create a Infinte Size
que.put(11)
que.put(22)
que.put(33)
print(que)
# print(len(que))
while not que.empty():
    i=que.get()
    print(i)

