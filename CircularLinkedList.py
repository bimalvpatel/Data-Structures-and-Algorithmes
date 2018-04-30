class Node:

    def __init__(self,data=None,next=None):
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

    def hasNext(self):
        return self.next != None

class CircularLinkedList():

    def __init__(self):
        self.head = None

    def insertAtBegorEnd(self,data,pos=False):
        newNode = Node(data)
        newNode.setNext(newNode)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() != self.head:
                current = current.getNext()
            current.setNext(newNode)
            newNode.setNext(self.head)
            if pos:
                self.head = newNode

    def insertAtPos(self,data,pos):
        if pos < 0 or pos > self.lengthoflist():
            print("Incorrect Position")
            return
        else:
            if pos == 0:
                self.insertAtBegorEnd(data,True)
            elif pos == self.lengthoflist():
                self.insertAtBegorEnd(data)
            else:
                count = 0
                current = self.head
                newNode = Node(data)
                while count < pos -1:
                    current = current.getNext()
                    count += 1
                newNode.setNext(current.getNext())
                current.setNext(newNode)

    def deleteAtBeg(self):
        if self.head == None:
            return "List is Empty"
        else:
            current = self.head
            if current == current.getNext():
                self.head = None
                return current.getData()
            while current.getNext() != self.head:
                current = current.getNext()
            current.setNext(self.head.getNext())
            result = self.head.getData()
            self.head = current.getNext()
            return result

    def deleteAtEnd(self):
        if self.head == None:
            return "List is Empty"
        else:
            current = self.head
            if current == current.getNext():
                self.head = None
                return current.getData()
            prev = None
            while current.getNext() != self.head:
                prev = current
                current = current.getNext()
            prev.setNext(self.head)
            current.setNext(None)
            return current.getData()

    def deleteAtPos(self,pos):
        if self.head == None:
            return "List is Empty"
        elif pos < 0 or pos > self.lengthoflist()-1:
            return "Incorrect Position"
        else:
            if pos == 0:
                return self.deleteAtBeg()
            elif pos == self.lengthoflist()-1:
                return self.deleteAtEnd()
            else:
                current = self.head
                prev = None
                count = 0
                while count < pos:
                    count += 1
                    prev = current
                    current = current.getNext()
                prev.setNext(current.getNext())
                current.setNext(None)
                return current.getData()

    def deleteAtVal(self,val):
        if self.head == None:
            return "List is Empty"
        if self.head.getData() == val:
            return self.deleteAtBeg()
        else:
            current = self.head
            prev = None
            while current.getNext() != self.head:
                if current.getData() == val:
                    prev.setNext(current.getNext())
                    current.setNext(None)
                    return current.getData()
                prev = current
                current = current.getNext()
        return str(val) + " is not in list"

    def lengthoflist(self):
        current = self.head
        if current == None:
            return 0
        count = 1
        while current.getNext() != self.head:
            count += 1
            current = current.getNext()
        return count

    def printList(self):
        if self.head == None:
            return
        current = self.head
        print(current.getData())
        while current.getNext() != self.head:
            current = current.getNext()
            print(current.getData())

if __name__ == "__main__":
    cll = CircularLinkedList()
    while (True):
        print("\nCircular Linked List Operations\n")
        print("1. Insert At Beginning")
        print("2. Insert At End")
        print("3. Insert At Position")
        print("4. Delete At Beginning")
        print("5. Delete At End")
        print("6. Delete At Position")
        print("7. Delete by Value")
        print("8. Length of List")
        print("9. Print List")
        n = int(raw_input("Enter Your Choice: "))
        if n == 1:
            data = int(raw_input("Enter Value: "))
            cll.insertAtBegorEnd(data,True)
        elif n == 2:
            data = int(raw_input("Enter Value: "))
            cll.insertAtBegorEnd(data)
        elif n == 3:
            data = int(raw_input("Enter Value: "))
            pos = int(raw_input("Enter Position: "))
            cll.insertAtPos(data, pos)
        elif n == 4:
            print("Deleted Value :" + str(cll.deleteAtBeg()))
        elif n == 5:
            print("Deleted Value: " + str(cll.deleteAtEnd()))
        elif n == 6:
            pos = int(raw_input("Enter position to delete: "))
            print("Deleted Value: " + str(cll.deleteAtPos(pos)))
        elif n == 7:
            val = int(raw_input("Enter Value to delete: "))
            print("Deleted Value: " + str(cll.deleteAtVal(val)))
        elif n == 8:
            print("Length : " + str(cll.lengthoflist()) + "\n")
        elif n == 9:
            cll.printList()
        elif n == 0:
            break
        else:
            pass

