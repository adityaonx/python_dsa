class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    def print_queue(self):
        tmp=self.first
        while tmp:
            print(tmp.value)
            tmp=tmp.next
    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
        else:
            self.last.next=new_node
        self.last=new_node
        self.length+=1
    def dequeue(self):
        if self.length==0:
            return None
        out=self.first.value
        self.first=self.first.next
        return out
    
my_queue=Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.dequeue()
my_queue.print_queue()