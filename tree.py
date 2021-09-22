class Node :
    def __init__(self, data, left=None, right=None) :
        self.data = data
        self.left = left
        self.right = right

global start
global root_node
global parent_node

start = Node(None)
root_node = start.right
parent_node = start.right

''' binary search tree insert '''

def insert(root, node) :
    
    # tree가 비어있을 때
    if (root == None) : 
        start.right = node

    # 알맞은 삽입 위치 찾기
    # 현재 위치보다 삽입숫자가 작으면 왼쪽에, 크면 오른쪽에
    # recursion
    elif (root.data < node.data) :
        if (root.right == None) :
            root.right = node
        else :
            insert(root.right, node)
    elif (root.data > node.data) :
        if (root.left == None) :
            root.left = node
        else :
            insert(root.left, node)

    # 해당 숫자가 있는 경우
    elif (root.data == node.data) :
        print("이미 있는 숫자 입니다.")


''' binary search tree delete '''

def delete(prnt, root, num) :

    # 삭제할 숫자 찾았을 때
    if (root.data == num) :
        # 오른쪽 subtree 중 가장 왼쪽 node를 삭제할 숫자 자리에 옮긴다.
        if (root.right != None) :
            if(root.right.left == None) :
                root.data = root.right.data
                root.right = root.right.right
            else :
                prnt = root.right
                pos_node = root.right.left
                while (pos_node.left != None) :
                    prnt = pos_node
                    pos_node = pos_node.left
                root.data = pos_node.data
                prnt.left = pos_node.right

        # 오른쪽 자식이없는 경우
        # 왼쪽 subtree 중 가장 오른쪽 node를 삭제할 숫자 자리에 옮긴다.
        elif (root.left != None) :
            if (root.left.right == None) :
                root.data = root.left.data
                root.left = root.left.left
            else :
                prnt = root.left
                pos_node = root.left.right
                while (pos_node.right != None) :
                    prnt = pos_node
                    pos_node = pos_node.right
                root.data = pos_node.data
                prnt.right = pos_node.left

        # 왼쪽, 오른쪽 자식 모두 없는 경우(terminal node 삭제)
        else :
            if (prnt.data == num) :
                start.right = None
            elif (prnt.data < num) :
                prnt.right = None
            else :
                prnt.left = None
                
    # 삭제할 숫자를 못찾았을 때
    
    # 삭제할 숫자가 현재 위치보다 큰 경우
    # -> 오른쪽 subtree에 대해서 delete 함수 진행
    elif (root.data < num) :
        delete(root, root.right, num)

    # 삭제할 숫자가 현재 위치보다 작은 경우
    # -> 왼쪽 subtree에 대해서 delete 함수 진행
    else :
        delete(root, root.left, num)
        
''' binary search tree search '''

def search(root, num) :
    
    # 트리가 비어있는 경우
    if (root == None) :
        return

    # 입력받은 숫자를 찾은 경우
    elif (root.data == num) :
        print(num, "을 찾았습니다!")
        return True
    
    # 입력받은 숫자를 찾지 못한 경우 
    else :
        # 숫자가 현재 위치보다 클 때
        # 오른쪽 자식이 있으면 오른쪽 subtree에 대해 search함수 다시 진행
        # 자식이 없으면 찾는 숫자는 없는 것!
        if (root.data < num) :
            if (root.right != None) :
                search(root.right, num)
            else :
                print(num, "은 없는 숫자 입니다.")
                return False
            
        # 숫자가 현재 위치보다 작을 때
        # 왼쪽 자식이 있으면 왼쪽 subtree에 대해 search함수 다시 진행
        # 자식이 없으면 찾는 숫자는 없는 것!
        elif (root.data < num) :
            if (root.left != None) :
                search(root.left, num)
            else :
                print(num, "은 없는 숫자 입니다.")
                return False

''' binary search tree print - preorder, inorder, postorder '''

# preorder
def print_tree_pre(root) :
    if (root != None) :
        print(root.data, end = ' ')
        print_tree_pre(root.left)
        print_tree_pre(root.right)

# inorder
def print_tree_in(root) :
    if (root != None) :
        print_tree_in(root.left)
        print(root.data, end = ' ')
        print_tree_in(root.right)

# postorder
def print_tree_post(root) :
    if (root != None) :
        print_tree_post(root.left)
        print_tree_post(root.right)
        print(root.data, end = ' ')

# tree의 노드 수를 세는 함수
# tree가 비어있는지 아닌지를 확인하기 위해 사용
def count(root, count_num) :
    if (root != None) :
        count_num += 1
        count(root.left, count_num)
        count(root.right, count_num)
    return count_num

# insert, delete, search, print를 선택해 해당 함수를 수행하는 main함수
def main() :
    while 1 :
        cnt = 0
        root_node = start.right
        c = count(root_node, cnt)
        root_node = start.right
        
        order = str(input("insert, delete, search, print, quit : "))

        # 삽입
        if order == 'insert' :
            insert_num = int(input("insert number : "))
            new_node = Node(insert_num)
            insert(root_node, new_node)
            root_node = start.right

        # 삭제
        if order == 'delete' :
            if c == 0 :
                print("트리가 비어있습니다.")
            else :
                delete_num = int(input("delete number : "))
                while (search(root_node, delete_num) == False) :
                    root_node = start.right
                    if search(root_node, delete_num) == False :
                        root_node = start.right
                        print("없는 숫자 입니다. 다른 숫자를 입력하세요")
                        delete_num = int(input("delete number : "))
                root_node = start.right
                parent_node = start.right
                delete(parent_node, root_node, delete_num)
                root_node = start.right
                parent_node = start.right

        # 탐색
        if order == 'search' :
            if c == 0 :
                print("트리가 비어있습니다.")
            else :
                search_num = int(input("search number : "))
                search(root_node, search_num)
                root_node = start.right

        # 출력
        if order == 'print' :
            if c == 0 :
                print("트리가 비어있습니다.")
            else :
                print("preorder  : ", end = ' ')
                print_tree_pre(root_node)
                root_node = start.right
                print()
            
                print("inorder   : ", end = ' ')
                print_tree_in(root_node)
                root_node = start.right
                print()
            
                print("postorder : ", end = ' ')
                print_tree_post(root_node)
                root_node = start.right
                print()

        #종료
        if order == 'quit' :
            break
