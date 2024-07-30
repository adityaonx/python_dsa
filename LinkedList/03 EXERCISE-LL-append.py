class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self,append_value):
        append_node = Node(append_value)
        if self.head is None:
            self.head=append_node
            self.tail=append_node
        else:  
            self.tail.next=append_node
            self.tail = append_node
        self.length+=1
        
        
 
my_linked_list = LinkedList(4)
print("BEFORE")
my_linked_list.print_list()

my_linked_list.append(5)
print("AFTER")
my_linked_list.print_list()



                                                                                                                    