# If your not understand this code paste in --> https://pythontutor.com/render.html#mode=edit   here and checjk
class Node():

    def __init__(self,data):
        self.data =data
        self.pointer=None

class LinkedList():

    def __init__(self):
        self.head=None

    def add(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
        else:
            curr = self.head
            while ( curr.pointer is not None):
                curr = curr.pointer

            curr.pointer = newnode

    def print(self):
        curr = self.head

        while (curr is not None):
            print(curr.data)
            curr = curr.pointer

ll= LinkedList()
ll.add(1)
ll.add(3)
ll.add(4)
ll.print()



# ============================================================================
    #    +-------------------------+                  +-------------------------+                   +-------------------------+
    #    |        LinkedList       |                  |            Node           |                   |            Node           |
    #    +-------------------------+                  +-------------------------+                   +-------------------------+
    #    |    head: -------------- | ---+             |         data: 1          |                   |         data: 3          |
    #    +-------------------------+    |             +-------------------------+                   +-------------------------+
    #                                    |             |     pointer: ---------- | --------------- |     pointer: ---------- | ----------> None
    #                                    |             +-------------------------+                   +-------------------------+
    #                                    |                                                                      ^
    #                                    |                                                                      |
    #                                    |                                                                      |
    #                                    |                                                                      |
    #                                    |                                                                      +--------------- None
    #                                    |
    #                                    v
    #    +-------------------------+
    #    |            Node           |
    #    +-------------------------+
    #    |         data: 4          |
    #    +-------------------------+
    #    |     pointer: None        |
    #    +-------------------------+


