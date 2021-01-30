#1052
#두 정수(a, b)를 입력받아 a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
a, b = input().split()
a = int(a)
b = int(b)
if a != b :
    print(1)
else :
    print(0)

#1053
#1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
a = int(input())
print(int(not(a)))  # 논리 연산자 not = ~아니다,부정의 의미 / 참이면 거짓, 거짓이면 참

#1054
#두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
a, b = input().split()
a = int(a)
b = int(b)
if a and b == 1 :   # 논리 연산자 and = ~이고, 그리고의 의미 / 둘 다 참이어야 한다
    print(1)
else :
    print(0)

#1055
#두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
if a or b == 1 :
    print(1)
else :
    print(0)
    
#1056
#두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
if a != b :
    print(1)
else :
    print(0)

#1057
#두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
if a == b :
    print(1)
else :
    print(0)

#1058
#두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
a,b = input().split()
a = int(a)
b = int(b)
if a==0 and b == 0 :
    print(1)
else :
    print(0)
    
#1059
#입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
a = int(input())
a1 = int(~a)    # 비트부정 ~ => 1은 0으로 0은 1로 변경
print(a1)

#1060
#입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
a,b = input().split()
a = int(a)
b = int(b)
print(a & b)    # 비트논리곱 & => 둘다 1이면 1