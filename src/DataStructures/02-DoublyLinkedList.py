class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        
class DoublyLinkedList:
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

    def print_schema(self):
        tmp=self.head
        if tmp is not None:
            print("head.value",tmp.value)
            if tmp.prev!=None:
                print("head.prev",tmp.prev.value)
            print("tail.value",self.tail.value)
            if self.tail.prev!=None:
                print("tail.prev",self.tail.prev.value)
            print("head.next",tmp.next)
            print("tail.next",self.tail.next)
            print("length",self.length)

    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    def pop(self):
        if self.head is None:
            return None
        popped=self.tail.value
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        self.length-=1
        return popped
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head:
            self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node
        self.length+=1

    def pop_first(self):
        if self.length<=0:
            return None
        if self.length!=1:
            self.head.prev=None
        popped=self.head.value
        self.head=self.head.next
        self.length-=1
        return popped

    def get(self,get_index):
        if get_index<0 or get_index>self.length-1:
            return None
        tmp=self.head
        for _ in range(get_index):
            tmp=tmp.next
        return tmp.value
    
    def set(self,set_index,value):
        if set_index<0 or set_index>=self.length:
            return None
        tmp=self.head
        for _ in range(set_index):
            tmp=tmp.next
        tmp.value=value
        return True
    def insert(self,insert_index,value):
        if insert_index<0 or insert_index>self.length:
            return None
        new_node=Node(value)
        tmp=self.head
        prev=None
        for _ in range(insert_index):
            prev=tmp
            tmp=tmp.next
        if insert_index==self.length:
            self.tail=new_node
        if insert_index==0:
            self.head=new_node
        else:
            prev.next=new_node
        new_node.prev=prev
        new_node.next=tmp
        self.length+=1

    def remove(self,remove_index):
        if  remove_index<0 or remove_index>=self.length:
            return None
        tmp=self.head
        if remove_index==self.length-1:
            self.tail=self.tail.prev
            self.tail.next=None
        elif remove_index==0:
            self.head=self.head.next
            self.head.prev=None
        else:
            for _ in range(remove_index):
                pre=tmp
                tmp=tmp.next
            pre.next=tmp.next
            tmp.next.prev=pre.next
        self.length-=1
        
        
my_ll=DoublyLinkedList(5)
my_ll.append(4)
my_ll.append(3)
my_ll.append(3)
my_ll.append(3)
my_ll.remove(1)
my_ll.print_list()
my_ll.print_schema()