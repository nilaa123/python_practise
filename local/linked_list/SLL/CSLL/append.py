class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        temp=self.head
        result=''
        while temp:
            result+=str(temp.data)
            temp=temp.next
            if temp==self.head:
                break
            result+='->'
        return result
    
    def append(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
            new_node.next=self.head
        self.length+=1
        return self.head
    

c=CSLL()
print(c)
c.append(1)
print(c)
c.append(2)
c.append(3)
print(c)
