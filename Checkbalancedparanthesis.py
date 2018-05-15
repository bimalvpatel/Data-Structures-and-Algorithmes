class Node:

        def __init__(self,data,next=None):
            self.data = data
            self.next = next

        def setData(self,data):
            self.data = data

        def getData(self):
            return self.data

        def setNext(self,next):
            self.next = next

        def getNext(self):
            return self.next

class Stack:

    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        temp = self.head
        self.head = self.head.getNext()
        return temp.getData()

    def isEmpty(self):
        return self.head == None

    def peek(self):
        return self.head.getData()

    def getSize(self):
        current = self.head
        len = 0
        while current != None:
            len += 1
        return len

def matches(top,symbol):
    opening = "({["
    closing = ")}]"
    return opening.index(top) == closing.index(symbol)

def checkSymbolBalance(input):
    symbolstack = Stack()
    for symbol in input:
        if symbol in ["(","{","["]:
            symbolstack.push(symbol)
        else:
            if symbolstack.isEmpty():
                return False
            top = symbolstack.pop()
            if not matches(top,symbol):
                return False
    return symbolstack.isEmpty()

if __name__ == "__main__":
    print(checkSymbolBalance("([])"))
    print(checkSymbolBalance("{{([][])}()}"))