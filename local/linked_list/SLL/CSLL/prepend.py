class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def prepend(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        self.length+=1
        return self.head