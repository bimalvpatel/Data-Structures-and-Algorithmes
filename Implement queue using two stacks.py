'''

Implement Queue with 2 stacks

'''

class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

class Queue:

    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enqueue(self,item):
        self.instack.push(item)

    def dequeue(self):
        if self.outstack.isEmpty():
            while not self.instack.isEmpty():
                self.outstack.push(self.instack.pop())
        return self.outstack.pop()

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(15)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(20)
    q.enqueue(25)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())