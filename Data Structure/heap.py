#함수문제! 함수 나오면 안변해있어.......

list = ['t','n', 'n', 'n', 'n', 'n '] #print용 리스트
L = ['t'] #heap list

def print_tree(L) :
    print(L)
    length = len(L)
    for i in range (0,length) :
        list[i] = L[i]
    print("     ", list[1])
    print("      |")
    print("  --------")
    print("  |      |")
    print(" ", list[2], "    ", list[3])
    print("  |")
    print("-----")
    print("|   |")
    print(list[4], " ", list[5])

def insert(L, n) : 
    
    L = L + [n]
    
    print_tree(L)
    index = len(L)-1
    
    while index != 1 :
        if L[index] > L[index//2] :
            temp = L[index//2]
            L[index//2] = L[index]
            L[index] = temp
        index = index//2
        print_tree(L)
    print(L)
    return L

def delete():
    if len(L) == 1 :
        print("Heap is empty")

    else :
        print("delete : [", L[1], "]")
        L[1] = L[len(L)-1]
        L = L[0:len(L)-1]
        print(L)

        #delete 후 sorting
        i=1
        while 1 :
            if i*2 > len(L)-1 :
                break
            elif i*2 == len(L)-1 :
                if L[i] < L[i*2] :
                    temp = L[i]
                    L[i] = L[i*2]
                    L[i*2] = temp
                break
            else :
                if L[i*2] > L[(i*2)+1] :
                    max = L[i*2]
                    index = i*2
                else :
                    max = L[(i*2)+1]
                    index = (i*2)+1

                if max > L[i] :
                    temp = L[i]
                    L[i] = max
                    L[index] = temp
                i = index
    print(L)
    


