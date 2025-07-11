class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0
    
    def print_all(self):
        if self.first:
            print("head",self.first.value)
        if self.last:
            print("tail",self.last.value)
        print("length",self.length)
        curr=self.first
        while curr:
            if curr.next is None:
                print(curr.value)
            else:
                print(curr.value,end="->")
            curr=curr.next

    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
        else:
            self.last.next=new_node
        self.last=new_node
        self.length+=1
        return True
    
    def dequeue(self):
        if self.length==0:
            return False
        if self.length==1:
            self.last=None
        deq=self.first.value
        self.first=self.first.next
        self.length-=1
        return deq


q=Queue()
q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
print("dequeue",q.dequeue())
# print("dequeue",q.dequeue())
# print("dequeue",q.dequeue())
q.print_all()