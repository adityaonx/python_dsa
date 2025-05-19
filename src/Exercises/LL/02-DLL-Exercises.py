class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DLL:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head==new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    def swap_first_last(self):
        if self.length<=1:
            return None
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def print_list(self):
        tmp=self.head        
        while tmp is not None:
            # if tmp.prev:
            #     print("tmp.prev",tmp.prev.value)
            # else:
            #     print("tmp.prev None")
            # if tmp.next:
            #     print("tmp.next",tmp.next.value)
            # else:
            #     print("tmp.next None")
            print("tmp.value",tmp.value)
            print("------------------")
            tmp=tmp.next

    def print_schema(self):
        tmp=self.head
        if tmp is not None:
            print("head.value",tmp.value)
            if tmp.prev!=None:
                print("head.prev",tmp.prev.value)
            # print("tail.value",self.tail.value)
            # if self.tail.prev!=None:
                # print("tail.prev",self.tail.prev.value)
            print("head.next",tmp.next)
            # print("tail.next",self.tail.next)
            print("length",self.length)

    
    def reverse(self):
        tmp=self.head
        while tmp:
            tmp.prev,tmp.next = tmp.next , tmp.prev
            tmp=tmp.prev
        self.head,self.tail=self.tail,self.head

    def check_pal(self):
        left=self.head
        right=self.tail
        for _ in range((self.length//2)+1):
            if left.value!=right.value:
                return False
            left=left.next
            right=right.prev
        return True

    def swap_pair(self):
        if self.length<=1:
            return False
        tmp=self.head
        while tmp and tmp.next:
            prev=tmp.prev
            post=tmp.next
            tmp.next=post.next
            if post.next:
                post.next.prev=tmp
            tmp.prev=post 
            post.next=tmp
            post.prev=prev
            if prev:
                prev.next=post
            tmp=tmp.next
        self.head=self.head.prev

    
            
dll=DLL(1)
dll.append(2)
dll.append(3)
# dll.append(4)
# dll.append(5)
# dll.append(6)
# dll.append(7)
# dll.append(8)

dll.swap_pair()
dll.print_list()
# dll.print_schema()