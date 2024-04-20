# Linked list direct approch

# class NODE():

#     def __init__(self,data):
#         self.data =data
#         self.pointer = None

#     def __str__(self):
#         return "mmmmm"
# node1=NODE(1)
# node2=NODE(2)
# node3=NODE(3)

# print(node1.data)
# print(node1.pointer)
# print(node1) #---> if we use with that str function it would only give us only hexa decimal aaddreess


class linked():

    def __init__(self,data):
        self.data=data
        self.pointer=None
Node1 = linked(22)
Node2 = linked(345)
Node3= linked(65)

Node1.pointer=Node2
Node2.pointer=Node3

print(Node1.data)
print(Node1.pointer)
print(Node1)

curr = Node1

while curr is not None:
    print(curr.data)
    curr =curr.pointer 

# print(curr)




# ==========================================================

    #    +-------------------------+
    #    |          Node1          |
    #    +-------------------------+
    #    |    data: 22             |
    #    |    pointer: --------->  | --> Node2
    #    +-------------------------+

    #    +-------------------------+
    #    |          Node2          |
    #    +-------------------------+
    #    |    data: 345            |
    #    |    pointer: --------->  | --> Node3
    #    +-------------------------+

    #    +-------------------------+
    #    |          Node3          |
    #    +-------------------------+
    #    |    data: 65             |
    #    |    pointer: None        |
    #    +-------------------------+


#        +-------------------------+        +-------------------------+        +-------------------------+
#        |          Node1          |        |          Node2          |        |          Node3          |
#        +-------------------------+        +-------------------------+        +-------------------------+
#        |    data: 22             |        |    data: 345            |        |    data: 65             |
#        |    pointer: --------->  | -----> |    pointer: --------->  | -----> |    pointer: None        |
#        +-------------------------+        +-------------------------+        +-------------------------+
#              |                                       |                                    ^
#              |                                       |                                    |
#              |                                       |                                    |
#              +---------------------------------------+                                    |
#                                                                                            |
#                                                                                            |
# +-------------------------+         +-------------------------+       +-------------------------+
# |          curr           |         |          curr           |       |          curr           |
# +-------------------------+         +-------------------------+       +-------------------------+
# |     Node1 (start)       |         |        Node2            |       |        Node3 (end)      |
# +-------------------------+         +-------------------------+       +-------------------------+
# |   Print data: 22        |         |   Print data: 345       |       |    Print data: 65       |
# +-------------------------+         +-------------------------+       +-------------------------+
# |  Move to Node2          |         |   Move to Node3         |       |    Move to None          |
# +-------------------------+         +-------------------------+       +-------------------------+
