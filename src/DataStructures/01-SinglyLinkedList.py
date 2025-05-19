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
        
        while tmp is not None:
            print(tmp.value)
            tmp=tmp.next
    def append(self,value):
        tmp=self.head
        pre=self.head
        while tmp is not None:
            pre=tmp
            tmp=tmp.next
        new_node=Node(value)
        pre.next=new_node
        self.tail=new_node
        if self.length==0:
            self.head=new_node
        self.length+=1
    def pop(self):
        if self.length==0:
            return False
        tmp=self.head
        pre=self.head
        while tmp.next is not None:
            pre=tmp
            tmp=tmp.next
        val=tmp.value
        pre.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return val

    def print_schema(self):
        tmp=self.head
        if tmp is not None:
            print("head.value",tmp.value)
            print("tail.value",self.tail.value)
            print("head.next",tmp.next)
            print("tail.next",self.tail.next)
            print("length",self.length)

    def remove(self,index):
        if index<0 or index>=self.length:
            return False
        tmp=self.head
        if index==0:
            self.head=tmp.next
            if self.length==1:
                self.tail=None
        else:
            pre=self.head
            for _ in range(index):
                pre=tmp
                tmp=tmp.next
            pre.next=tmp.next
            if tmp.next is None:
                self.tail=pre
        tmp.next=None
        self.length-=1

    def reverse(self):
        pre=None
        tmp=self.head
        self.tail=self.head
        while tmp:
            post=tmp.next
            tmp.next=pre
            pre=tmp
            tmp=post
        self.head=pre
            
        
        
my_ll=LinkedList(5)
my_ll.append(4)
my_ll.append(3)
my_ll.append(2)
my_ll.append(1)
# print("remove",my_ll.remove(4))
my_ll.reverse()
print("-----------LinkedList----------")
my_ll.print_list()
print("-----------Schema----------")
my_ll.print_schema()