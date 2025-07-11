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

def isParBal(s):
        s1=Stack()
        for i in s:
             s1.push(i)
        s2=Stack()
        for _ in range(len(s1.list)):
            if s1.peek(-1)==")":
                s2.push(s1.pop())
        for _ in range(len(s2.list)):
            if s1.peek(-1)=="(":
                s2.pop()
                s1.pop()
        if len(s1.list)==0 and len(s2.list)==0:
            return True
        else:
            return False
str1='()))(('
print(isParBal(str1))

