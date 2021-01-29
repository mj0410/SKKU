#받아온 데이터 정리 위해 필요
import re

import mazeGUI
import StackQueue

from random import randint

class Node:
    def __init__(self, data, up=None, down=None, left=None, right=None, bread=False):
        self.data = data
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.bread = bread

#10X10 maze 생성
def createMaze(maze) :

    #노드 생성
    for i in range(10) :
        for j in range(10) :
            maze[i][j]=Node(maze[i][j])

    #미로를 linked list로 연결
    for i in range(10) :
        for j in range(10) :
            if (i==0) :
                if (j==0) :
                    maze[i][j].right = maze[i][j+1]
                    maze[i][j].down = maze[i+1][j]
                elif (j==9) :
                    maze[i][j].left = maze[i][j-1]
                    maze[i][j].down = maze[i+1][j]
                else :
                    maze[i][j].right = maze[i][j+1]
                    maze[i][j].left = maze[i][j-1]
                    maze[i][j].down = maze[i+1][j]
            elif (i==9) :
                if (j==0) :
                    maze[i][j].right = maze[i][j+1]
                    maze[i][j].up = maze[i-1][j]
                elif (j==9) :
                    maze[i][j].left = maze[i][j-1]
                    maze[i][j].up = maze[i-1][j]
                else :
                    maze[i][j].left = maze[i][j-1]
                    maze[i][j].right = maze[i][j+1]
                    maze[i][j].up = maze[i-1][j]
            elif (j==0) :
                maze[i][j].right = maze[i][j+1]
                maze[i][j].up = maze[i-1][j]
                maze[i][j].down = maze[i+1][j]
            elif (j==9) :
                maze[i][j].left = maze[i][j-1]
                maze[i][j].up = maze[i-1][j]
                maze[i][j].down = maze[i+1][j]
            else :
                maze[i][j].right = maze[i][j+1]
                maze[i][j].left = maze[i][j-1]
                maze[i][j].up = maze[i-1][j]
                maze[i][j].down = maze[i+1][j]

#미로 출력
def printMaze(maze) :
    for i in range(10) :
        for j in range(10) :
            if maze[i][j].data == 'U' :
                print('U ', end=' ')
            elif maze[i][j].data == 'D' :
                print('D ', end=' ')
            elif maze[i][j].data == 0 :
                print('■', end=' ')
            else :
                print('□', end=' ')
        print()


#txt파일 읽어와서 숫자만 남긴 후 배열로 정리            
def readTXT() :
    global data
    data = []
    txt = open('A.txt')
    d=txt.read().splitlines()
    for i in range(10) :
        number = re.findall("\d+", d[i])
        for j in range(len(number)) :
            number[j] = int(number[j])
        data = data +[number]
    return data

def pathFinder (start, end) :

    #print("Q = ", end=' ')
    #routeQ.print()
    #print("S = ", end=' ')
    #routeS.print()

    if (start%10 == 0) :
        pointer = maze[(int(start/10))-1][9]
    else :
        pointer = maze[int(start/10)][int((start%10)-1)]

    if (end%10 == 0) :
        des = maze[(int(end/10))-1][9]
    else :
        des = maze[int(end/10)][int((end%10)-1)]

    des.data = end

    if (pointer.up !=None) :
        if (pointer.up.data == end) :
            routeS.push(pointer.data)
            routeS.push(end)
            routeQ.enqueue(pointer.data)
            routeQ.enqueue(end)
            print("미로찾기 종료!")
            return
    if (pointer.down != None) :
        if (pointer.down.data == end) :
            routeS.push(pointer.data)
            routeS.push(end)
            routeQ.enqueue(pointer.data)
            routeQ.enqueue(end)
            print("미로찾기 종료!")
            return
    if (pointer.left != None) :
        if (pointer.left.data == end) :
            routeS.push(pointer.data)
            routeS.push(end)
            routeQ.enqueue(pointer.data)
            routeQ.enqueue(end)
            print("미로찾기 종료!")
            return
    if (pointer.right != None) :
        if (pointer.right.data == end) :
            routeS.push(pointer.data)
            routeS.push(end)
            routeQ.enqueue(pointer.data)
            routeQ.enqueue(end)
            print("미로찾기 종료!")
            return

    check_list=[]

    if (pointer.up != None) :
        if (pointer.up.bread == False and pointer.up.data != 0):
            check_list.append(pointer.up.data)
    if (pointer.down != None) :
        if (pointer.down.bread == False and pointer.down.data != 0):
            check_list.append(pointer.down.data)
    if (pointer.left != None) :
        if (pointer.left.bread == False and pointer.left.data != 0):
            check_list.append(pointer.left.data)
    if (pointer.right != None) :
        if (pointer.right.bread == False and pointer.right.data != 0):
            check_list.append(pointer.right.data)

    #print("start = ", start, " check = ", check_list)

    #=============================================================
    # 1. 갈 수 있는 방향 : 0개.
    # 되돌아가기.
    if (len(check_list) == 0) : 
        # 지금 서 있는 곳이 출발지인지 확인.
        if (pointer.data == 'U') : # 출발지가 맞다면 오류라는 것 출력하기.
            print('미로에 오류가 있습니다. 목적지까지 갈 수 없습니다.')
            return
            
        
        # 빵조각을 남긴다. 
        pointer.bread = True
        # 현재 위치를 routeQ 에만 기록한다. (위치가 겹치면 기록하지 않는다.)
        routeQ.enqueue(start)
                
        start = routeS.peek()
        routeS.pop()
        routeQ.enqueue(start)
        
        pathFinder (start, end)

    #=============================================================
    # 2. 갈 수 있는 방향 : 1개.
    elif (len(check_list) == 1): 
        # 빵조각을 남긴다. 
        pointer.bread = True
        # 현재 위치를 routeS과 routeQ 에 기록한다.
        if (routeS.isEmpty()) :
            routeS.push(start)
        else :
            if (routeS.peek() != start) :
                routeS.push(start)

        if (routeQ.isEmpty()) :
            routeQ.enqueue(start)
        else :
            if (routeQ.peek() != start) :
                routeQ.enqueue(start)

        start = check_list[0]
        
        pathFinder (start, end)

    #=============================================================
    # 3. 갈 수 있는 방향 : 2개 이상.
    elif (len(check_list) >= 2): #선택지가 2개 이상인 경우
        dist_to_wall_list=[]
        for i in range(len(check_list)) :
            dist_to_wall_list.append(0)
            #<- 갈 수 있는 노드가 벽으로 부터 얼마나 떨어져있는지 그 값 저장
            
        # 빵조각을 남긴다.
        pointer.bread = True
        
        # 현재 위치를 routeS과 routeQ 에 기록한다.
        if (routeS.isEmpty()) :
            routeS.push(start)
        else :
            if (routeS.peek() != start) :
                routeS.push(start)

        if (routeQ.isEmpty()) :
            routeQ.enqueue(start)
        else :
            if (routeQ.peek() != start) :
                routeQ.enqueue(start)
        
        for i in range(len(check_list)): 
            #갈 수 있는 노드가 left나 right인 경우 6이상과 미만으로 나누어 벽까지의 거리를 구해 dist_to_wall_list[] 에 저장
            if (abs(start - check_list[i])==1) : 
                # right
                if (check_list[i] > start):
                    if (check_list[i]%10 == 0) :
                        dist_to_wall_list[i] = int(check_list[i]%10)
                    else :
                        dist_to_wall_list[i] = 10 - int(check_list[i]%10)
                # left
                else:
                    dist_to_wall_list[i] = int(check_list[i]%10)-1
                
            #갈 수 있는 노드가 up이나 down인 경우 5이상과 미만으로 나누어 벽까지 거리를 구해 dist_to_wall_list[] 에 저장     
            elif (abs(start - check_list[i])==10) :
                # up
                if (check_list[i] < start) :
                    dist_to_wall_list[i] = int(check_list[i]/10)
                # down    
                else:
                    dist_to_wall_list[i] = 9 - int(check_list[i]/10)

        # dist_to_wall_list에서 거리가 가장 짧은 노드를 찾아 그 주소값을 position에 저장
        smallest = dist_to_wall_list[0]
        #largest = dist_to_wall_list[0]
        #rand_index = randint(0,len(dist_to_wall_list)-1)
        
        small_index = 0
        #large_index = 0
        
        for i in range(len(dist_to_wall_list)):
            if (smallest > dist_to_wall_list[i]):
                smallest = dist_to_wall_list[i]
                small_index = i

        '''
        for i in range(len(dist_to_wall_list)):
            if (largest < dist_to_wall_list[i]):
                largest = dist_to_wall_list[i]
                large_index = i
        '''

        #print("벽까지의 거리 = ", dist_to_wall_list, " 짧은 거리 = ", dist_to_wall_list[small_index])

        #짧은 곳으로 이동
        start = check_list[small_index]

        #넓은 곳으로 이동
        #start = check_list[large_index]
                
        #랜덤하게 이동
        #start = check_list[rand_index]

        pathFinder (start, end)

    

def main() :
    global maze
    global start
    global U
    global end

    #maze 배열 생성
    a=[]
    for i in range(100) :
        a=a+[i+1]

    readTXT()

    for i in range(len(data)) :

        maze = [[ a[j] for j in range(i, i+10) ] for i in range(0,100,10)]
        createMaze(maze)

        #출발지, block, 목적지 표시

        for j in range(10) :
            for k in range(10) :
                if (maze[j][k].data == data[i][0]) :
                    maze[j][k].data = 'U'
                    start = (j*10)+k+1
                    U = (j*10)+k+1
                elif (maze[j][k].data == data[i][len(data[i])-1]) :
                    maze[j][k].data = 'D'
                    end = (j*10)+k+1
                for l in range (1, len(data[i])-1) :
                    if (maze[j][k].data == data[i][l]) :
                        maze[j][k].data = 0

        printMaze(maze)
        #print("start = ", start, " end = ", end)

        global routeQ
        routeQ = StackQueue.queue()
        global routeS
        routeS = StackQueue.stack()

        pathFinder(start, end)

        #print("routeQ = ", end='')
        print("route = ", end='')
        routeQ.print()

        mazeGUI.PrintMaze()

        print()
        
