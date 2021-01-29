# 변수 설정
global a
a = []

# 리스트 입력 받음
N = int(input("입력할 숫자의 개수 : "))
for i in range(N) :
    num = int(input("숫자를 입력하세요 : "))
    a.append(num)

# binary search는 정렬 된 data에 사용할 수 있는 탐색방법
# 정렬이 필요하므로 selection sort로 정렬한다

for i in range(N) :
    min_index = i
    for j in range(i+1, N) :
        if (a[j] < a[min_index]) :
            min_index = j
    temp = a[min_index]
    a[min_index] = a[i]
    a[i] = temp


### binary search ###
    
value = int(input("찾고싶은 숫자를 입력하시오 : "))

# 탐색 시작점, 끝점 설정
left = 0
right = len(a)-1

# 탐색
while(left <= right) :
    mid = (left+right)//2
    
    if left == right :
        if (value != a[mid]) :
            print(value, "은(는) 없습니다.")
            break
        
    if value == a[mid] :
        print(value, "을(를) 찾았습니다!")
        print(value, "은(는) ", mid+1, "번째 원소입니다.")
        break
    
    elif value < a[mid] :
        right = mid - 1
        
    else :
        left = mid + 1

if(left > right) :
    print(value, "은(는) 없습니다.")


    
    
