
class Node:
    def __init__(self, data):
        self._left = None
        self._data = data
        self._right = None


    def insert(self, data):

        newNode = Node(data)

        if self._data:
            if self._data > data:
                if self._left is not None:
                    self._left.insert(data)
                else:
                    self._left = newNode

            else:
                if self._right is not None:
                    self._right.insert(data)
                else:
                    self._right = newNode
        else:
            self._data = data

    def lookUp(self, data):
        # from root to find the node with data value
        if self._data > data:
            return self._left.lookUp(data)
        elif self._data < data:
            return self._right.lookUp(data)
        else:
            return self

    def getData(self):
        return self._data

    def getChildCount(self):
        cnt = 0
        if self._left is not None:
            cnt += 1

        if self._right is not None:
            cnt += 1

        return cnt

    def delete(self, data, parent = None):
        if self._data > data:
            self._left.delete(data, self)
        elif self._data < data:
            self._right.delete(data, self)
        else:
            childCount = self.getChildCount()
            delNode = None
            successorNode = None

            if childCount == 0:
                delNode = self
                if parent._left == self:
                    parent._left = None
                else:
                    parent._right = None

            elif childCount >= 1:

                successorParentNode = None

                if self._left is not None:
                    successorNode = self._left
                    while successorNode._right is not None:
                        successorParentNode = successorNode
                        successorNode = successorNode._right

                    if successorParentNode is not None:
                        successorParentNode._right = successorNode._left
                    else:
                        self._left = None
                else:
                    successorNode = self._right
                    while successorNode._left is not None:
                        successorParentNode = successorNode
                        successorNode = successorNode._left

                    if successorParentNode is not None:
                        successorParentNode._left = successorNode._right
                    else:
                        self._right = None
                self._data = successorNode._data

                delNode = successorNode

            del delNode

    def printAll(self):

        if self._left is not None:
            self._left.printAll()

        print(self._data)

        if self._right is not None:
            self._right.printAll()


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

import copy

print('********')
root1 = copy.deepcopy(root)
root1.delete(1)
root1.printAll()

print('********')
root2 = copy.deepcopy(root)
root2.delete(14)
root2.printAll()

print('********')
root3 = copy.deepcopy(root)
root3.delete(3)

root3.printAll()
