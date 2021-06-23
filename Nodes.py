
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

    def insertNode(self,curNode,newValue):

        if curNode.value > newValue and curNode.left == None:
            curNode.left = Node(newValue)
        elif curNode.value < newValue and curNode.right == None:
            curNode.right = Node(newValue)
        elif curNode.value > newValue and curNode.left != None:
            curNode.left.insertNode(curNode.left,newValue)
        elif curNode.value < newValue and curNode.right != None:
            curNode.left.insertNode(curNode.right,newValue)

testValue = Node(1)
testValue.insertNode(testValue,-20)
testValue.insertNode(testValue,20)
testValue.insertNode(testValue,19)
print(testValue.right.left.value)