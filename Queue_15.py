#List type example

queue = [1,2,3,4,5]
print(queue)
#DEqUEUE
queue.append(6)
queue.append(7)
print(queue)
#Dequeue
queue.pop(0)
queue.pop(0)
print(queue)
#Checking queue is Empty or Not
print(len(queue) == 0)

#Example 2 class of queue

from queue import Queue

q=Queue()
#Enqueue
q.put(1)
q.put("Heloo")
#Dequeue
a=q.get()   #This will delete a first value
print(a)
print(q.empty()) # beacuse value is there

Qu = Queue(maxsize=3)
Qu.put(10)
Qu.put(20)
Qu.put(111)
print (Qu.full()) #It's full
