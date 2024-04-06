# Creating a Queue using list
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
print(queue)
queue.pop(0)
queue.pop(0)
print(len(queue)==0)
print(queue)
print("==================================")

#In this method we can insert but we can delete a POP( not mention a Index)

queue=[]
queue.insert(0,100)
queue.insert(0,200)
queue.insert(0,300)
queue.insert(0,400)
print(queue)
queue.pop()
queue.pop()
print(queue)