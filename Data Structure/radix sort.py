# 정렬하고 싶은 숫자의 개수를 입력
N = int(input("입력할 숫자의 개수 : "))

# sorting을 위한 list 설정
sort_radix = [] # bucket list
sort = [] # bucket
a = [] # 입/출력용

# list initialization
sort_radix = []
for i in range(10) :
    sort_radix.append([])
sort = []

# 정렬할 숫자를 입력받음
for i in range(N) :
    num = int(input("숫자를 입력하세요 : "))
    a.append(num)

# 입력받은 숫자 중 가장 큰 숫자의 자릿수를 구한다
# 가장 큰 숫자 = max, 자릿수 = count
max = a[0]
for i in range(1, N) :
    if (max < a[i]) :
        max = a[i]

temp = max
count = 0
while (temp != 0) :
    count+=1
    temp = temp//10

# 각 자릿수를 구하기 위해 수를 나누는 데 쓰이는 상수
# 첫번째는 1로 나눈 수의 나머지(1의자리)
# 두번째는 10으로 나눈 수의 나머지(10의자리) ....
div = 1

print()

### radix sort ###

for i in range(count) :
    for j in range(10) :
        for k in range(N) :
            # 10^count의 자리수(1의자리, 10의자리...)를 구해 sort에 넣음
            if ((a[k]//div)%10 == j) :
                sort.append(a[k])
        sort_radix[j] = sort
        # sort는 각 bucket이므로 다음 bucket으로 넘어가기 전에 초기화
        sort = []
    # 각 자리수 별로 분류가 끝나면 분류된 bucket 출력 (과정을 보기 위한 용도입니다)
    print("[",i+1,"] BUCKET")
    for j in range(10) :
        print(sort_radix[j])
    print()

    # bucket에 나누어진 숫자를 다시 리스트로 합침
    t = 0
    for j in range(10) :
        for k in range(N) :
            if ( len(sort_radix[j]) == 0 ) :
                break
            if(t == N) :
                break
            a[t] =  sort_radix[j][k]
            t += 1
            if (k==len(sort_radix[j])-1) :
                break
        if (t == N) :
            break

    # 다음 자리수 분배를 위해 bucket과 bucker list를 초기화
    sort_radix = []
    for i in range(10) :
        sort_radix.append([])
    sort = []

    # 다음 자리수의 나머지를 알아야 하므로 나누는 수에 10을 곱함
    # ( ex)1의자리 -> 10의자리...)
    div *= 10

# 정렬된 리스트 출력
print("radix sort result = ", a)
