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

            
    def get(self,index):
        curr=self.head
        if index>=self.length or index<0:
            return None
        for i in range(index):
            curr=curr.next
        return curr

    def set(self,index,data):
        temp=self.get(index)
        if temp is not None:
            temp.data=data
            return True
        return False

    def __str__(self):
        curr=self.head
        result=""
        while curr is not None:
            if curr.next is not None:
                result=result+str(curr.data)+' -> '
            else:
                result=result+str(curr.data)
            curr=curr.next
        return result

l1=LinkedList()
l1.append(0)
l1.append(1)
l1.append(2)
print(l1)
