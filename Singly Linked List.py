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

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBeg(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node

    def insertAtEnd(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.hasNext():
                current = current.getNext()
            current.setNext(node)

    def insertAtPos(self,data,pos):
        if pos < 0 or pos > self.lengthoflist():
            print("Incorrect Position")
            return
        else:
            if pos == 0:
                self.insertAtBeg(data)
            elif pos == self.lengthoflist():
                self.insertAtEnd(data)
            else:
                node = Node(data)
                current = self.head
                count = 0
                while count < pos - 1:
                    count += 1
                    current = current.getNext()
                node.setNext(current.getNext())
                current.setNext(node)

    def deleteAtBeg(self):
        if self.head == None:
            return "List is Empty"
        temp = self.head
        self.head = self.head.getNext()
        return temp.getData()

    def deleteAtEnd(self):
        if self.head == None:
            return "List is Empty"
        current = self.head
        prev = None
        while current.hasNext():
            prev = current
            current = current.getNext()
        if prev == None:
            self.head = None
        else:
            prev.setNext(None)
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
        current = self.head
        prev = None
        if current.getData() == val:
            self.head = self.head.getNext()
            return current.getData()
        else:
            while current != None:
                if current.getData() == val:
                    prev.setNext(current.getNext)
                    return current.getData()
                prev = current
                current = current.getNext()
        return str(val) + " is not in List"

    def lengthoflist(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()


if __name__ == "__main__":
    ll = LinkedList()
    while(True):
        print("\nLinked List Operations\n")
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
            ll.insertAtBeg(data)
        elif n == 2:
            data = int(raw_input("Enter Value: "))
            ll.insertAtEnd(data)
        elif n == 3:
            data = int(raw_input("Enter Value: "))
            pos = int(raw_input("Enter Position: "))
            ll.insertAtPos(data,pos)
        elif n == 4:
            print("Deleted Value :"+str(ll.deleteAtBeg()))
        elif n == 5:
            print("Deleted Value: "+str(ll.deleteAtEnd()))
        elif n == 6:
            pos = int(raw_input("Enter position to delete: "))
            print("Deleted Value: "+str(ll.deleteAtPos(pos)))
        elif n == 7:
            val = int(raw_input("Enter Value to delete: "))
            print("Deleted Value: "+str(ll.deleteAtVal(val)))
        elif n == 8:
            print("Length : "+str(ll.lengthoflist()) + "\n")
        elif n == 9:
            ll.printList()
        elif n == 0:
            break
        else:
            pass



