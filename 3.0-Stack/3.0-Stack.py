class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.height=0

    def printAll(self):
        if self.top:
            print("top",self.top.value)
        if self.bottom:
            print("bottom",self.bottom.value)
        print("height",self.height)
        curr=self.top
        while curr:
            print(curr.value)
            curr=curr.next

    def push(self,value):
        new_node=Node(value)
        if self.height==0:self.bottom=new_node
        else:new_node.next=self.top
        self.top=new_node
        self.height+=1
        return True
    
    def pop(self):
        if self.height==0:
            return False
        if self.height==1:
            self.bottom=None
        popped=self.top.value
        self.top=self.top.next
        self.height-=1
        return popped
mystack=Stack()
mystack.push(5)
mystack.push(4)
mystack.push(3)
mystack.push(2)
mystack.push(1)
print("popped",mystack.pop())
mystack.printAll()
