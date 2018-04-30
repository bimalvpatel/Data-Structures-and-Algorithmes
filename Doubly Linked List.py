class Node:

    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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

    def setPrev(self,prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def hasPrev(self):
        return self.prev != None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insertAtBeg(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.hasNext():
                current = current.getNext()
            current.setNext(newNode)
            newNode.setPrev(current)

    def insertAtPos(self,data,pos):
        if pos < 0 or pos > self.lengthoflist():
            print("Incorrect Position")
            return
        else:
            if pos == 0 or self.head == None:
                self.insertAtBeg(data)
            elif pos == self.lengthoflist():
                self.insertAtEnd(data)
            else:
                newNode = Node(data)
                count = 0
                current = self.head
                while count < pos-1:
                    count += 1
                    current = current.getNext()
                newNode.setNext(current.getNext())
                newNode.setPrev(current)
                current.getNext().setPrev(newNode)
                current.setNext(newNode)

    def deleteAtBeg(self):
        if self.head == None:
            return "List is Empty"
        else:
            current = self.head
            self.head = self.head.getNext()
            if self.head != None:
                self.head.setPrev(None)
            current.setNext(None)
            return current.getData()

    def deleteAtEnd(self):
        if self.head == None:
            return "List is Empty"
        else:
            current = self.head
            while current.hasNext():
                current = current.getNext()
            current.getPrev().setNext(None)
            current.setPrev(None)
            return current.getData()

    def deleteAtPos(self,pos):
        if pos < 0 or pos > self.lengthoflist()-1:
            return "Incorrect Position"
        else:
            if pos == 0:
                return self.deleteAtBeg()
            elif pos == self.lengthoflist()-1:
                return self.deleteAtEnd()
            else:
                current = self.head
                count = 0
                while count < pos:
                    count += 1
                    current = current.getNext()
                current.getPrev().setNext(current.getNext())
                current.getNext().setPrev(current.getPrev())
                current.setPrev(None)
                current.setNext(None)
                return current.getData

    def deleteAtVal(self,val):
        current = self.head
        if current.getData() == val:
            return self.deleteAtBeg()
        else:
            while current != None:
                if current.getData() == val:
                    current.getPrev().setNext(current.getNext())
                    if current.getNext() != None:
                        current.getNext().setPrev(current.getPrev())
                    current.setNext(None)
                    current.setPrev(None)
                    return current.getData()
                current = current.getNext()
        print(str(val) + " is not in the list")

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def lengthoflist(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

if __name__ == "__main__":
    dll = DoublyLinkedList()
    while (True):
        print("\nDoubly Linked List Operations\n")
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
            dll.insertAtBeg(data)
        elif n == 2:
            data = int(raw_input("Enter Value: "))
            dll.insertAtEnd(data)
        elif n == 3:
            data = int(raw_input("Enter Value: "))
            pos = int(raw_input("Enter Position: "))
            dll.insertAtPos(data, pos)
        elif n == 4:
            print("Deleted Value :" + str(dll.deleteAtBeg()))
        elif n == 5:
            print("Deleted Value: " + str(dll.deleteAtEnd()))
        elif n == 6:
            pos = int(raw_input("Enter position to delete: "))
            print("Deleted Value: " + str(dll.deleteAtPos(pos)))
        elif n == 7:
            val = int(raw_input("Enter Value to delete: "))
            print("Deleted Value: " + str(dll.deleteAtVal(val)))
        elif n == 8:
            print("Length : " + str(dll.lengthoflist()) + "\n")
        elif n == 9:
            dll.printList()
        elif n == 0:
            break
        else:
            pass