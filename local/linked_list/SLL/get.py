class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def get(self,index):
        curr=self.head
        if index>=self.length or index<0:
            return None
        for i in range(index):
            curr=curr.next
        return curr
