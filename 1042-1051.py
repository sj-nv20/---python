#1042
#정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
a, b = input().split()
a = int(a)
b = int(b)
print(a//b)

#1043
#정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
a, b = input().split()
a = int(a)
b = int(b)
print(a%b)

#1044
#정수를 1개 입력받아 1만큼 더해 출력해보자.
a = int(input())
print(a+1)

#1045
#정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("%.2f" % (a/b))

#1046
#정수 3개를 입력받아 합과 평균을 출력해보자.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
a1 = a+b+c
print(a1)
print("%.1f" % (a1/3))

#1047
#정수 1개를 입력받아 2배 곱해 출력해보자.
a = int(input())
print(a*2)

#1048
#정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b) # 비트연산자 - 쉬프트연산 = 2를 곱하는 효과가 있다 / 비트를 왼쪽으로 2번 이동

#1049
#두 정수(a, b)를 입력받아 a가 b보다 크면 1을, a가 b보다 작거나 같으면 0을 출력하는 프로그램을 작성해보자.
a, b = input().split()
a = int(a)
b = int(b)
if a > b :
    print(1)
else :
    print(0)

#1050
#두 정수(a, b)를 입력받아 a와 b가 같으면 1을, 같지 않으면 0을 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
if a == b:
    print(1)
else :
    print(0)

#1051
#두 정수(a, b)를 입력받아 b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
if a <= b:
    print(1)
else :
    print(0)