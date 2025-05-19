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

    def find_middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.value
    
    def has_loop(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    def kth_node(self,k):
        slow=self.head
        fast=self.head
        for _ in range(k):
            if fast==None:
                return False
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        return slow.value
    
    def partition_list(self,x):
        dum1=Node(0)
        dum2=Node(0)
        pre1=dum1
        pre2=dum2
        current=self.head
        while current:
            if x>current.value:
                pre1.next=current
                pre1=current
            else:
                pre2.next=current
                pre2=current
            current=current.next
        pre1.next=None
        pre2.next=None
        pre1.next=dum2.next
        self.head=dum1.next

    def print_schema(self):
        tmp=self.head
        if tmp is not None:
            print("head.value",tmp.value)
            print("tail.value",self.tail.value)
            print("head.next",tmp.next)
            print("tail.next",self.tail.next)
            print("length",self.length)

    def remove_duplicates(self):
        if self.length<=1:
            return False
        pre=self.head
        curr=self.head
        values=set()
        while curr:
            if curr.value not in values:
                values.add(curr.value)
                pre=curr
            else:
                pre.next=curr.next
                self.length-=1
            curr=curr.next
        self.tail=pre
    
    def bin_to_dec(self):
        sum=0
        tmp=self.head
        for i in range(self.length-1,-1,-1):
            sum= sum + (tmp.value*(2**(i)))
            tmp=tmp.next
        return sum
    
    def reverse_btw(self,start_index,end_index):
        if self.length<=1:
            return None
        dum=Node(0)
        dum.next=self.head
        pre=dum
        for _ in range(start_index):
            pre=pre.next
        tmp=pre.next
        for _ in range(end_index-start_index):
            post=tmp.next
            tmp.next=post.next
            post.next=pre.next
            pre.next=post
        self.head=dum.next
ll=LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.reverse_btw(1,3)
# print("--------LinkedList---------")
ll.print_list()#12345
# ll.print_schema()