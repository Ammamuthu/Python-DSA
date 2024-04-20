class Node():
    def __init__(self,data):
        self.data = data
        self.pointer = None
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        
    def add(self,data):
        newnode = Node(data)
        
        if (self.head == None):
            self.head = newnode
        else:
            curr = self.head

            while(curr.pointer is not None):
                curr = curr.pointer
            curr.pointer = newnode
    
    def print(self):

        curr =self.head

        while (curr is not None):
            print(curr.data)
            curr =curr.pointer
        
        print("----------")

            
    def remove(self,data):
        if (self.head is not None):
            if(self.head.data == data):
                self.head = self.head.pointer 
            else:
                curr = self.head
                while (curr.pointer is not None and data != curr.pointer.data):
                    curr =curr.pointer
                # If we don't have the value in our list
                if curr.pointer is not None:
                    curr.pointer = curr.pointer.pointer

                else:
                    print(data , "There is no data ")

        else:
            print(" List is Empty")
          
        
LL = LinkedList()
LL.add(1)
LL.add(12)
LL.add(7)
LL.add(8)
LL.print()
LL.remove(13)
LL.print()

# ==========================================================================================

            #  +-----------------------------------------------------------+
            #  |                      LinkedList                           |
            #  +-----------------------------------------------------------+
            #  |                       head: ----------------------------- | ----> Node1
            #  +-----------------------------------------------------------+
            #                 |
            #                 |
            #                 v
            #  +-----------------------------------------------------------+       +-----------------------------------------------------------+
            #  |                          Node                             |       |                          Node                             |
            #  +-----------------------------------------------------------+       +-----------------------------------------------------------+
            #  |                        data: 1                            |       |                        data: 12                           |
            #  |                      pointer: --------------------------- | ----> |                      pointer: --------------------------- | ----> Node3
            #  +-----------------------------------------------------------+       +-----------------------------------------------------------+
            #                 |                                                         |
            #                 |                                                         |
            #                 v                                                         v
            #  +-----------------------------------------------------------+       +-----------------------------------------------------------+
            #  |                          Node                             |       |                          Node                             |
            #  +-----------------------------------------------------------+       +-----------------------------------------------------------+
            #  |                        data: 7                            |       |                        data: 8                            |
            #  |                      pointer: --------------------------- | ----> |                      pointer: --------------------------- | ----> None
            #  +-----------------------------------------------------------+       +-----------------------------------------------------------+
            #                 |
            #                 |
            #                 v
            #  +-----------------------------------------------------------+
            #  |                          Node                             |
            #  +-----------------------------------------------------------+
            #  |                           None                            |
            #  +-----------------------------------------------------------+
             

# +-------------------+     +-------------------+     +-------------------+     +-------------------+     +-------------------+
# | Head (None)       | ----> | Node (data: 1)     | ----> | Node (data: 3)     | ----> | Node (data: 4)     | ----> | None             |
# +-------------------+     +-------------------+     +-------------------+     +-------------------+     +-------------------+
#                    |             |                     |                     |                     |
#                    |             v                     v                     v                     v
# +-------------------+     +-------------------+     +-------------------+     +-------------------+     +-------------------+
# | curr (Initially     | ----> | Node (data: 1)     | ----> | Node (data: 3)     | ----> | Node (data: 4)     | ----> | None             |
# +-------------------+     +-------------------+     +-------------------+     +-------------------+     +-------------------+
#                    |             |                     |                     |
#                    |             v                     v (Traverse)             v (Remove node 3)
# +-------------------+     +-------------------+     +-------------------+     +-------------------+     +-------------------+
# | prev (None)       | ----> | Node (data: 1)     | ----> | Node (data: 3)     | ----> | Node (data: 4)     | ----> | None             |
# +-------------------+     +-------------------+     +-------------------+ (becomes prev)         +-------------------+

# +-------------------+
# |                   |
# |   Start           |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   Check if head   |
# |   is not None     |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   Is head.data    |
# |   equal to data?  |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   Yes             |
# |   Update head     |
# |   to head.pointer |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   No              |
# |   Initialize curr |
# |   to head         |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   While curr      |
# |   has a pointer   |
# |   and data is not |
# |   equal to        |
# |   curr.pointer    |
# |   .data           |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   Update curr to  |
# |   curr.pointer    |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   If curr.pointer |
# |   is not None     |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   Update curr     |
# |   pointer to      |
# |   curr.pointer   |
# |   .pointer        |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   Else            |
# |   Print message   |
# |   indicating no   |
# |   data found      |
# |                   |
# +-------------------+
#         |
#         v
# +-------------------+
# |                   |
# |   End             |
# |                   |
# +-------------------+
