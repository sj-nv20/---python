#1061
#입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
a,b = input().split()
a = int(a)
b = int(b)
ab = a | b  # | => 비트 논리합(or)
print(ab)

#1062
#입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
a,b = input().split()
a = int(a)
b = int(b)
ab = a ^ b  # ^ => 비트 논리적 배타합(xor)
print(ab)

#1063
#입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
print(a if a>b else b)  #삼항연산자

#1064
#입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
ab = (a if a < b else b)
print( ab if ab < c else c)

#1065
#세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0 :
    print(a)
if b%2 == 0 :
    print(b)
if c%2 == 0 :
    print(c)
