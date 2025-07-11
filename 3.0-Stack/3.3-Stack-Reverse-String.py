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

def revString(s):
    s1=Stack()
    for i in s:
            s1.push(i)
    reversed=""
    for _ in range(len(s1.list)):
         reversed+=s1.list.pop()
    return reversed
        
str1='12345'
print(revString(str1))#54321

