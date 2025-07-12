class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0