class Node():
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None
class DLL():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def print_list(self):
        curr=self.head
        while curr:
            print(curr.value)
            curr=curr.next
    def print_all(self):
        curr=self.head
        if self.head:
            print("head",self.head.value)
        else:
            print("head : None")
        
        if self.tail:
            print("tail",self.tail.value)
        else:
            print("tail : None")
        print("length : ",self.length)
        while curr:
            if curr.prev:
                print("curr.prev.value",curr.prev.value)
            else:
                print('curr.prev = None')
            print("curr.value:",curr.value)
            if curr.next:
                print("curr.next.value",curr.next.value)
            else:
                print('curr.next = None')
            curr=curr.next
        curr=self.head
        while curr:
            if not curr.next:
                print(curr.value)
            else:
                print(curr.value,end=" -> ")
            curr=curr.next

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def pop(self):
        if self.length==0:
            return False
        if self.length==1:
            self.head=None
        popped=self.tail.value
        self.tail=self.tail.prev
        self.length-=1
        return popped
    
    def prepend(self,value):
        if self.length==0:
            self.append(value)
            return True
        new_node=Node(value)
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length==0:
            return False
        if self.length==1:
            self.tail=None
        popped=self.head.value
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        self.length-=1
        return popped
    
    def get(self,index):
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr

    def set(self,index,value):
        if index>=self.length:
            return False
        node=self.get(index)
        node.value=value
        return True
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            self.prepend(value)
            return True
        if index==self.length:
            self.append(value)
            return True
        else:
            new_node=Node(value)
            curr=self.get(index)
            prev=curr.prev
            prev.next=new_node
            new_node.prev=prev
            new_node.next=curr
            curr.prev=new_node
            self.length+=1
            return True
        
    def remove(self,index):
        if index<0 or index>=self.length:
            return False
        if index==0:
            self.pop_first()
            return True
        if index==self.length-1:
            self.pop()
            return True
        curr=self.get(index)
        prev=curr.prev
        post=curr.next
        prev.next=post
        post.prev=prev
        self.length-=1
        return True

            
        
newDll=DLL()
newDll.append(1)
newDll.append(2)
# newDll.append(3)
# newDll.append(4)
# newDll.append(5)

def swapFirstNLast(ls):
    if ls.length in [0,1]:
        return False
    curr_val=ls.head.value
    ls.head.value=ls.tail.value
    ls.tail.value=curr_val
    return True
swapFirstNLast(newDll)
newDll.print_all()
