class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#리스트에 값 저장
head = Node(None)

#기타 node 지정
start_node = head.next
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
            if start_node == None :
                break
            count += 1
            start_node = start_node.next

        start_node = head.next

        #리스트가 비어있는 경우
        if count == 0 :
            head.next = Node(addnum)
        #리스트에 원소가 있는 경우
        else :
            new_node = Node(addnum)
            #입력받은 수의 자리 찾기
            while 1 :
                if addnum <= start_node.data :
                    new_node.next = start_node
                    pre_node.next = new_node
                    break
                else :
                    if start_node.next == None :
                        start_node.next = new_node
                        break
                    pre_node = start_node
                    start_node = start_node.next

        start_node = head.next

        #입력받은 숫자가 삽입된 리스트 출력
        while 1 :
            print(start_node.data, end=' ')
            if start_node.next == None :
                break
            start_node = start_node.next
        print()
        
        start_node = head.next
        pre_node = head

    if order == 'del' :
        
        count=0

        #리스트 길이 파악
        while 1 :
            if start_node == None :
                break
            count += 1
            start_node = start_node.next
        start_node = head.next

        #리스트가 비어있는 경우
        if count == 0 :
            print("리스트가 비어있습니다")

        #리스트에 원소가 있는 경우
        else :
            delnum = eval(input("Delete Number : "))
            while 1 :
                if delnum != start_node.data :
                    pre_node = start_node
                    start_node = start_node.next
                    #입력한 숫자와 같은 숫자가 없는 경우
                    if start_node == None :
                        print("삭제할 숫자가 없습니다")
                        break
                else :
                    pre_node.next = start_node.next
                    break
                
        start_node = head.next
        pre_node = head

        #원소 삭제 후 리스트 출력
        if start_node == None :
            print("")
        else :
            while 1 :
                print(start_node.data, end=' ')
                if start_node.next == None :
                    break
                start_node = start_node.next
            print()
        
        start_node = head.next

    if order == 'quit' :
        break

