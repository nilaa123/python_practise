class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def __str__(self):
        current_node=self.head
        result=''
        while current_node.next:
            
            result+=(f"{current_node.data} ->")
            current_node=current_node.next
        result+=(f" {current_node.data}")
        return result
    
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current_node=self.head
            while current_node.next:
                current_node=current_node.next
            current_node.next=new_node
    
                          
l=LinkedList()
l.append(1)

l.append(2)

l.append(22)
print(l)