class Node:

    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def addNode(self,ele):
        if ele > self.data:
            if self.right == None:
                self.right = Node(ele)
            else:
                self.right.addNode(ele)
        else:
            if self.left == None:
                self.left = Node(ele)
            else:
                self.left.addNode(ele)

    def inordertraversal(self):
        global A
        if self.left:
            self.left.inordertraversal()
        A.append(self.data)
        if self.right:
            self.right.inordertraversal()

class BST:

    def __init__(self):
        self.root = None

    def createBST(self,ele):
        if self.root == None:
            self.root = Node(ele)
        else:
            self.root.addNode(ele)

    def inordertraversal(self):
        if self.root == None:
            return
        else:
            self.root.inordertraversal()

if __name__ == "__main__":
    bst = BST()
    A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
    for i in range(len(A)):
        bst.createBST(A[i])
    A = []
    bst.inordertraversal()
    print(A)