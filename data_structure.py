class Stack(object):
    def __init__(self,top = 0):
        self.top_pointer = top
        self.values = []
    def __str__(self):
        return "Stack:\n (pointer = {},value = {})".format(self.top_pointer,
                                                            self.top_pointer)
    def __eq__(self,o): return isinstance(o,Stack) and self.top_pointer == o.top_pointer

    def __ne__(self,o): return not self == o

class Queue(object):
    def __init__(self,front = 0,rear = -1,values = []):
        self.front = front
        self.rear = -1
        self.values = []
    def __str__(self): return "Queue:\n (front = %d,rear = %d)" %(self.front,self.rear)

    def __eq__(self,o): return  isinstance(o,Queue) and self.front == o.front and self.rear == o.rear and self.values == o.values

    def __ne__(self,o): return not self == o

class ChainNode(object):
    def __init__(self,value = None,prev = None,next = None):
        self.prev = prev
        self.next = next
        self.value = value
    def __str__(self): return "Chain Node: (prev = %s,next = %s,value = %s)" % (self.prev.content,self.next.content,self.content)

    def show(self): 
        if self.prev is None:
            return "| %s-> %s" % (self.value,self.next.value)
        if self.next is None:
            return "%s-> %s |" % (self.prev.value,self.value)
        return "%s-> %s ->%s" % (self.prev.show(),self.value,self.next.show())
    
    def __eq__(self,o): return isinstance(o,ChainNode) and self.value == self.value

    def __ne__(self,o): return not o == self

    def attach_to(self,next): self.next = next;next.prev = self
        
c1 = ChainNode("c1")
c2 = ChainNode("c2")
c3 = ChainNode("c3")

c1.attach_to(c2)
c2.attach_to(c3)
print(c1.show())