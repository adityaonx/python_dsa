
class Stack:
    def __init__(self):
        self.stack_list=[]

    def push(self,value):
        self.stack_list.append(value)
    def pop(self):
        if self.stack_list:
            return self.stack_list.pop()
        return None
    def is_empty(self):
        if len(self.stack_list)==0:
            return True
        return False
    def peek(self):
        return self.stack_list[-1]
    def print_items(self):
        for i in self.stack_list:
            print(i)

###P1.Check "(()))" balanced or Not
def bal_par(s1):
    stack=Stack()
    for i in s1:
        if i=="(":
            stack.push(i)
        elif i==")":
            if stack.is_empty() or stack.pop()!="(":
                return False
    return stack.is_empty()

# st1="(()"
# print(bal_par(st1))

###P2.Reverse string using stack
def reverse_str_stack(s2):
    stack=Stack()
    for i in range(len(s2)):
        stack.push(s2[i])
    rev_s2=""
    while not stack.is_empty():
        rev_s2+=stack.pop()
    print(rev_s2)

# st2="hello"
# reverse_str_stack(st2)

###P3. sort stack using one addition stack i.e sorted_stack
def stack_sort_stack(stk):
    sorted_stack=Stack()
    while not stk.is_empty():
        tmp=stk.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek()>tmp:
            stk.push(sorted_stack.pop())
        sorted_stack.push(tmp)
    while not sorted_stack.is_empty():
        print(sorted_stack.pop())

# stack1=Stack()
# stack1.push(5)
# stack1.push(3)
# stack1.push(4)
# stack1.push(1)
# stack1.push(2)
# stack_sort_stack(stack1)

class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    
    def enqueue(self,value):
        s1=self.stack1
        s2=self.stack2
        s1.append(value)
        for i in s1:
            s2.append(s1.pop())
    
    def dequeue(self):
        s2=self.stack2
        s2.pop()
    def print_queue(self):
        for i in self.stack2:
            print(i)
my_q=MyQueue()
my_q.enqueue(1)
my_q.enqueue(2)
my_q.enqueue(3)
my_q.enqueue(4)
my_q.dequeue()
my_q.print_queue()