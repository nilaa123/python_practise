class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

l=LinkedList()
l.append(1)
print(l.length)
print(l.tail.data)
l.append(2)
print(l.length)
print(l.tail.data)


