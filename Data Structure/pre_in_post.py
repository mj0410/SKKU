class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

node1 = Node('-')
node2 = Node('*')
node3 = Node('/')
node4 = Node('A')
node5 = Node('B')
node6 = Node('C')
node7 = Node('D')

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

#preorder

def preorder(node) :
    if node != None :
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node) :
    if node != None :
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def postorder(node) :
    if node != None :
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

print("preorder = ", end='')
preorder(node1)
print()
print("inorder = ", end='')
inorder(node1)
print()
print("postorder = ", end='')
postorder(node1)
