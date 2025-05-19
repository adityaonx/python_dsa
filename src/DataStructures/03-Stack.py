class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    def print_items(self):
        tmp=self.top
        while tmp:
            print(tmp.value)
            tmp=tmp.next    

    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.height+=1

    def pop(self):
        if self.height is None:
            return None
        tmp=self.top
        popped = tmp.value
        self.top=tmp.next
        self.height-=1
        return popped
    
    

my_stack=Stack(4)
my_stack.push(5)
# my_stack.pop()
# my_stack.pop()
my_stack.print_items()