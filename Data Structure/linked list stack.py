class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def isEmpty() :
    if (top == None) :
        return True
    else  :
        return False

def printStack(bottom) :
    temp = bottom
    print("Linked Stack : [", end=' ')
    while 1 :
        if temp == None :
            print(" ", end='')
            break
        print(temp.data, end=' ')
        if temp.next == None :
            break
        temp = temp.next
    print(']')

top = None
bottom = None

while 1 :
    order = str(input("push, pop, peak, quit : "))
    if order == 'push' :
        push = input("Push : ")
        new_node = Node(push)
        if isEmpty() :
            bottom = new_node
            top = new_node
        else :
            top.next = new_node
            top = top.next
        printStack(bottom)

    if order == 'pop' :
        if isEmpty() :
            print("isEmpty!")
        else :
            pre = bottom
            temp = bottom.next
            if bottom == top :
                bottom = None
                top = None
            else :
                while 1 :
                    if (temp.data == top.data) :
                        top = pre
                        top.next = None
                        break
                    pre = temp
                    temp = temp.next
            printStack(bottom)

    if order == 'peak' :
        if isEmpty() :
            print("isEmpty!")
        else :
            print("peak is ", top.data)

    if order == 'quit' :
        break
    
