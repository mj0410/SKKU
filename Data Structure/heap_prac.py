L = ['t']
L = L + [10]

print(L)
index = len(L)-1

while index != 1 :
    if L[index] > L[index//2] :
        temp = L[index//2]
        L[index//2] = L[index]
        L[index] = temp
    index = index//2
    print(L)

L = L + [45]

print(L)
index = len(L)-1

while index != 1 :
    if L[index] > L[index//2] :
        temp = L[index//2]
        L[index//2] = L[index]
        L[index] = temp
    index = index//2
    print(L)

L = L + [19]

print(L)
index = len(L)-1

while index != 1 :
    if L[index] > L[index//2] :
        temp = L[index//2]
        L[index//2] = L[index]
        L[index] = temp
    index = index//2
    print(L)

L = L + [11]

print(L)
index = len(L)-1

while index != 1 :
    if L[index] > L[index//2] :
        temp = L[index//2]
        L[index//2] = L[index]
        L[index] = temp
    index = index//2
    print(L)

L = L + [96]

print(L)
index = len(L)-1

while index != 1 :
    if L[index] > L[index//2] :
        temp = L[index//2]
        L[index//2] = L[index]
        L[index] = temp
    index = index//2
    print(L)


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


