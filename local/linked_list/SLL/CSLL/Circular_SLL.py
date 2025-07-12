class Node:
    def __init__(self,data=0):
        self.data=data
        self.next=None

class CSLL:
    def __init__(self,value):
        new_node=Node(value)
        new_node.next=new_node
        self.head=new_node
        self.tail=new_node
        self.length=1


cll=CSLL(1)
print(cll.head.next.data)
