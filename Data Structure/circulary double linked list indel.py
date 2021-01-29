class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

head = Node(None)
head.right = head
head.left = head
start_node = head.right
pre_node = head

#삽입, 삭제, 종료 선택
while 1 :
    order = str(input("add, del, quit : "))
    #삽입
    if order == 'add' :

        #삽입할 숫자 입력
        addnum = eval(input("Add Number : "))
        count=0

        #리스트 길이 파악
        while 1 :
            if start_node.data == None :
                break
            count += 1
            start_node = start_node.right

        start_node = head.right

        #리스트가 비어있는 경우
        if count == 0 :
            new_node = Node(addnum)
            head.right = new_node
            head.left = new_node
            new_node.right = head
            new_node.left = head
            
        #리스트에 원소가 있는 경우
        else :
            new_node = Node(addnum)
            #입력받은 수의 자리 찾기
            while 1 :
                if addnum <= start_node.data : #중간 혹은 앞에 삽입
                    new_node.right = start_node
                    new_node.left = pre_node
                    pre_node.right = new_node
                    start_node.left = new_node
                    break
                else :
                    if start_node.right == head : #맨 뒤에 삽입
                        start_node.right = new_node
                        new_node.left = start_node
                        new_node.right = head
                        head.left = new_node
                        break
                    pre_node = start_node
                    start_node = start_node.right

        start_node = head.right
        pre_node = head

        #입력받은 숫자가 삽입된 리스트 출력
        while 1 :
            print(start_node.data, end=' ')
            if start_node.right == head :
                break
            start_node = start_node.right
        print()
        
        start_node = head.right

    if order == 'del' :
        
        count=0

        #리스트 길이 파악
        while 1 :
            if start_node.data == None :
                break
            count += 1
            start_node = start_node.right
        start_node = head.right

        #리스트가 비어있는 경우
        if count == 0 :
            print("리스트가 비어있습니다")

        #리스트에 원소가 있는 경우
        else :
            delnum = eval(input("Delete Number : "))
            while 1 :
                if delnum != start_node.data :
                    pre_node = start_node
                    start_node = start_node.right
                    #입력한 숫자와 같은 숫자가 없는 경우
                    if start_node == head :
                        print("삭제할 숫자가 없습니다")
                        break
                else :
                    pre_node.right = start_node.right
                    start_node.right.left = pre_node
                    break
                
        start_node = head.right
        pre_node = head

        #원소 삭제 후 리스트 출력
        if start_node.data == None :
            print("")
        else :
            while 1 :
                print(start_node.data, end=' ')
                if start_node.right == head :
                    break
                start_node = start_node.right
            print()
        
        start_node = head.right

    if order == 'quit' :
        break
