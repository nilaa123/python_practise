class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def pop_first(self):
        if self.length==0:
            return None
        poped=self.head
        if self.length==1:
            self.head=None
            self.tail=None
            
        else:
            self.head=poped.next
            poped.next=None
        self.length-= 1
        return poped.data
            
