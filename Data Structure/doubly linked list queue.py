class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isEmpty() :
    if (front == None) :
        return True
    else  :
        return False

def printNode(front) :
    temp = front
    print("Linked Queue : [", end=' ')
    while 1 :
        if temp == None :
            print(" ", end='')
            break
        print(temp.data, end=' ')
        if temp.right == None :
            break
        temp = temp.right
    print(']')

front = None
rear = None

while 1 :
    order = str(input("en, de, peak, quit : "))
    if order == 'en' :
        en = input("Enqueue : ")
        new_node = Node(en)
        if isEmpty() :
            print("empty")
            front = new_node
            rear = new_node
        else :
            print("not empty")
            rear.right = new_node
            new_node.left = rear
            rear = rear.right
        printNode(front)

    if order == 'de' :
        if isEmpty() :
            print("isEmpty!")
        else :
            front = front.right
            printNode(front)

    if order == 'peak' :
        print("peak is ", front.data)

    if order == 'quit' :
        break
