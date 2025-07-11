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

st=Stack()
st.push(3)
st.push(2)
st.push(1)
st.print_stack()
st.pop()
st.print_stack()