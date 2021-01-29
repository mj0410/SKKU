list = ['t', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
order = str(input("원하는 위치를 입력하시오 : "))

index=0

while 1 :
    index += 1
    if list[index] == order :
        break

if index == len(list) :
    print("원하는 값이 없습니다")

elif index > 7 :
    print(list[index], "의 부모 노드는 : ", list[index//2])
    print("자식노드는 없습니다.")

elif index == 1 :
    print("root노드입니다.")
    print(list[index], "의 왼쪽 자식 노드는 : ", list[index*2])
    print(list[index], "의 오른쪽 자식 노드는 : ", list[(index*2)+1])

else :
    print(list[index], "의 부모 노드는 : ", list[index//2])
    print(list[index], "의 왼쪽 자식 노드는 : ", list[index*2])
    print(list[index], "의 오른쪽 자식 노드는 : ", list[(index*2)+1])
