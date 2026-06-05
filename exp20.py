class Node:
    def __init__(self , key):
        self.key = key
        self.left = None
        self.right = None

def insert(node , key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left , key)
    else:
        node.right = insert(node.right , key)
    return node

def deleteNode(root , key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left , key)
    elif root.key < key:
        root.right = deleteNode(root.right , key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
    
# Hey hello guys how are you doing