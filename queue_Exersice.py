queue=[]
def enqueue():
    human=int(input("Enter the Element that you want To add : "))
    queue.append(human)
def dequeue():
    if len(queue) != 0:
        queue.pop()
    else:
        print("Nothing In Here.")
def show():
    print(queue)
while True:
    usr=int(input("Enter 1 for add , 2 for del 3 for show , 4 for quit"))
    if usr == 1:
        enqueue()
    elif usr ==2:
        dequeue()
    elif usr == 3:
        show()
    else:
        break
print("Thank you ...........")
    