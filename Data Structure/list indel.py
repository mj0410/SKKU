L1 = [10, 20, 40, 50]
print(L1)

while (1) :
    order = str(input("Add, Del, Quit : "))
    if order == "add" :
        addnum = eval(input("Number : "))
        if len(L1) == 0 :
            L1 = [addnum]
        else :
            for i in range (0,len(L1)) :
                #같은 숫자가 있다면 이미 있다는 메세지
                if addnum == L1[i] :
                    print("같은 숫자가 있습니다")
                    break
                else :
                    #리스트 앞부터 차례로 크기를 비교
                    if addnum < L1[i] :
                        #입력한 숫자가 비교한 숫자보다 작을때 앞자리에 넣는다
                        L1 = L1+[L1[len(L1)-1]] #삽입 위해 list 길이 늘이기
                        for j in range (len(L1)-2, i, -1) :
                            #맨 뒤 숫자부터 하나씩 뒤로 밀기
                            L1[j] = L1[j-1]
                            print(L1)
                        L1[i]=addnum
                        break
            print(L1)

    if order == "del" :
        #리스트에 원소가 없을때 삭제할 수 없다는 메세지
        if len(L1) == 0 :
            print("삭제할 수 없습니다")
        else :
            delnum = eval(input("Number : "))
            for i in range (0, len(L1)) :
                #같은 숫자가 있다면 그 숫자를 삭제
                if delnum == L1[i] :
                    L1[i] = None
                    break
                #같은 숫자가 없다면 일치하는 수 없다는 메세지
                else :
                    if delnum < L1[i] :
                        print("일치하는 수가 없습니다")
                        break

    if order == "quit" :
        break
            
            
