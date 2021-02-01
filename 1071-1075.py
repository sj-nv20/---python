#1071
#정수가 순서대로 입력된다. 단 개수는 알 수 없다.
#0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
a = input().split()
for x in a :
    if int(x) == 0:
        break
    else :
        print(x)

#1072
#n개의 정수가 순서대로 입력된다. 단 n의 최대 개수는 알 수 없다. 
#n개의 입력된 정수를 순서대로 출력해보자.
n = int(input())
a = input().split()
b = map(int, a)
for x in b :
    print(x)
    
#1073
#정수가 순서대로 입력된다. 단 개수는 알 수 없다.
#0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
a = input().split()
for x in a :
    if int(x) == 0:
        break
    else :
        print(x)

#1074
#정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
a = int(input())
for x in range(a, 0, -1):   #range() => 지정된 범위의 값을 반환
    print(x)

#1075
#정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
a = int(input())
for x in range(a-1, -1, -1):   #range() => 지정된 범위의 값을 반환
    print(x)