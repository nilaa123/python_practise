class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def insert(self,value,index):
        new_node=Node(value)
        if index<0 or index>self.length:
            return False
        elif self.head==None:
            self.head=new_node
            self.tail=new_node
        elif index==0:
            new_node.next=self.head
            self.head=new_node
        elif index==self.length:
            self.tail.next=new_node
            self.tail=new_node
        else:
            current_node=self.head
            for i in range(index-1):
                current_node=current_node.next
            new_node.next=current_node.next
            current_node.next=new_node
        self.length+=1
        return True
            
        
ll = LinkedList()
ll.insert(10, 0)  # Inserts correctly
ll.insert(20, 1)  # Inserts at index 1
ll.insert(5, 1) 
print(ll.head.next.data)