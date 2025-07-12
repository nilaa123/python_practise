class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def search(self,target):
        curr=self.head
        index=0
        while curr is not None:
            if curr.data==target:
                return index
            curr=curr.next
            index+=1
        return -1
    
                