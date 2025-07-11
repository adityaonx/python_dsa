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

class Queue:
    def __init__(self):
        self.queue=Stack()
    def enqueue(self,value):
        self.queue.push(value)
    def dequeue(self):
        s1=self.queue
        if len(s1.list)==0:
            return False
        s2=Stack()
        for _ in range(len(s1.list)):
            s2.push(s1.pop())
        deq=s2.pop()
        for _ in range(len(s2.list)):
            s1.push(s2.pop())
        return deq
    def print_queue(self):
        for i in range(len(self.queue.list)):
            print(self.queue.list[i])

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.print_queue()