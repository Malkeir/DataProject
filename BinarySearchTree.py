


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key



def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

objs = Node(20)
objs = insert(objs,16)
objs = insert(objs,1)
objs = insert(objs,100)

inorder(objs)