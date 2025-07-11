class Stack:
    def __init__(self):
        self.list=list()
    
    def push(self,value):
        ls=self.list
        ls.append(value)
        return True
    def pop(self):
        ls=self.list
        if len(ls)==0:
            return False
        popped=ls.pop()
        return popped

    def peek(self,index):
        ls=self.list
        peeked=ls[index]
        return peeked

def stackSort(unsort):
    input_stack=Stack()
    for item in unsort:
        input_stack.push(item)

    sorted_stack=Stack()

    while len(input_stack.list)!=0:
        tmp=input_stack.pop()
        while len(sorted_stack.list)!=0 and sorted_stack.peek(-1)>tmp:
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(tmp)
    while len(sorted_stack.list)!=0:
        input_stack.push(sorted_stack.pop())
    
    while len(input_stack.list):
        print(input_stack.pop())
        

        
unsorted=[1,5,2,7,4]
stackSort(unsorted)

