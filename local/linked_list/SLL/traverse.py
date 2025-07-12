class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def traverse(self):
        curr=self.head
        while curr is not None:
            print(curr.data)
            curr=curr.next


l1=Linkedlist()
l1.head=Node(1)
l1.head.next=Node(2)
l1.head.next.next=Node(3)
l1.tail=l1.head.next.next
l1.length=3
l1.traverse()