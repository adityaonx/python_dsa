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
    def pop(self):
        if self.head is None:
            print("List is Empty, please insert a value first!")
            return None
        elif self.head.next is None:
            pop_value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return pop_value
        else:
            pop_value = self.tail.value
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            self.tail=temp
            self.tail.next = None
            self.length-=1
            return pop_value    
 
my_linked_list = LinkedList(4)
print("BEFORE append")
my_linked_list.print_list()


print("AFTER append")
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.print_list()

print("POP Value:",my_linked_list.pop())

print("AFTER POP")
my_linked_list.print_list()





                                                                                                                    