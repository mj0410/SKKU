stack = []
while 1 :
    order = str(input("push, pop, peak, quit : "))

    if order == 'push' :
        p = input("Push : ")
        stack = stack + [p]
        print(stack)

    if order == 'pop' :
        if len(stack)==0 :
            print("stack이 비어있습니다")
        else :
            stack = stack[0:len(stack)-1]
        print(stack)

    if order == 'peak' :
        if len(stack)==0 :
            print("stack이 비어있습니다")
        else :
            print("peak is ", stack[len(stack)-1])

    if order == 'quit' :
        break
