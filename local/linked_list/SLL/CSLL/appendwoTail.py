class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class CSLL:
    def __init__(self):
        self.head=None
        self.length=0

    def append(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.head.next=new_node
        else:
            curr=self.head
            for _ in range(self.length-1):
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head
        self.length+=1
        return self.head
    

c=CSLL()
c.append(0)
c.append(1)
print(c.head.data)
print(c.head.next.data)
