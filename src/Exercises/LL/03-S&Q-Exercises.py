
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


st1="(()"
print(bal_par(st1))

