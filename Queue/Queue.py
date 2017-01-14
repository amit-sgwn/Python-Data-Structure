'''
    Implementation of queue data structure in python
'''
class Queue:
    def __init__(self):
        self.items=[]
    def enque(self,item):
        self.items.insert(0,item)
    def deque(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items)==0

    def length(self):
        return len(self.items)
