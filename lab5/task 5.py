# Lab 5 - Artificial Intelligence
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# DFS using Stack
def dfs_stack(root):
    stack = [root]

    print("DFS using Stack:")
    while stack:
        node = stack.pop()
        print(node.value, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print()

def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

A.left = B
A.right = C
B.left = D
B.right = E

dfs_stack
print("Preorder Traversal:")
preorder(A)

print("\nInorder Traversal:")
inorder(A)

print("\nPostorder Traversal:")
postorder(A)