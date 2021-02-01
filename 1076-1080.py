#1076**
#영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.
a = ord(input())
b = ord('a')
while a>=b :
    print(chr(b), end = " ")
    b+=1

#1077
#정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
a = int(input())
for x in range(0, a+1, +1):   #range() => 지정된 범위의 값을 반환
    print(x)

#1078
#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
a = int(input())
sum = 0
for x in range(1, a+1) :
    if x%2 == 0:
        sum += x        
print(sum)

#1079
#'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
a = input().split()
for x in a :
    if x == 'q':
        print(x)
        break
    else :
        print(x)

#1080
#1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지 계속 더하는 프로그램을 작성해보자.
a = int(input())
sum = 0
for x in range(1, a+1) :
    sum+=x
    if sum >= a:
        print(x)
        break

