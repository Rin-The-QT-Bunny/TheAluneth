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