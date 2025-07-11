class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        tmp=self.head
        while tmp:
            print(tmp.value)
            tmp=tmp.next

    def prepend(self,value):
        if self.length == 0:
            new_node=Node(value)
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return True
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.length+=1
        return True

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.length+=1
            return True
        self.tail.next=new_node
        self.tail=new_node
        self.length+=1
        return True
    
    def popfirst(self):
        if self.length==0:
            return False
        popped_first=self.head.value
        self.head=self.head.next
        self.length-=1
        return popped_first
    
    def pop(self):
        if self.length==0:
            return False
        if self.length==1:
            popped=self.head.value
            self.head=None
            self.tail=None
            self.length-=1
            return popped
        tmp=self.head
        while tmp.next!=self.tail:
            tmp=tmp.next
        popped=self.tail.value
        self.tail=tmp   
        self.tail.next=None
        self.length-=1
        return popped

    def get(self,index):
        if index>=self.length:
            return False
        tmp=self.head
        for _ in range(index):
            tmp=tmp.next
        return tmp
    
    def set(self,index,value):
        if index<0 or index>=self.length:
            return False
        self.get(index).value=value
        return True
        
    def insert(self,index,value):
        if index>self.length:
            return False
        if index==self.length:
            self.append(value)
            return True
        if index==0:
            self.prepend(value)
            return True
        tmp=self.get(index-1)
        new_node=Node(value)
        new_node.next=tmp.next
        tmp.next=new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index>=self.length:
            return False
        if index==0:
            self.popfirst()
            return True
        if index==self.length-1:
            self.pop()
            return True
        tmp=self.get(index-1)
        tmp.next=tmp.next.next
        self.length-=1
        return True
    
    def reverse(self):
        if self.length in [0,1]:
            return False
        tmp=self.head
        self.head=self.tail
        self.tail=tmp
        prev=None
        while tmp:
            post=tmp.next
            tmp.next=prev
            prev=tmp
            tmp=post
        

newLL=LinkedList(1)
newLL.append(2)
newLL.append(3)
newLL.append(4)
newLL.reverse()
newLL.print_list()