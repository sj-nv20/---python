#1110
#입력받은 정수를 그대로 출력한다.
a = int(input())
print(a)

#1111
#어떤 정수가 입력되면 %를 붙여 출력하시오.
a = int(input())
print(a, '%' ,sep='')

#1112
#입력 받은 두 정수를 출력한다.
a ,b = map(int,input().split())
print(a,b)

#1113
#두 정수를 입력받아 순서를 바꿔서 출력하시오.
a ,b = map(int,input().split())
print(b,a)

#1114
#두 정수를 입력받아 합을 출력한다.
a ,b = map(int,input().split())
print(a+b)

#1115
#두 정수의 덧셈의 결과를 출력한다.
#두 수는 int 범위를 넘어선 64비트 정수형 값이다.
a ,b = map(int,input().split())
print(a+b)

#1116
#두 정수를 입력받아 아래와 같이 출력하시오.
# 예)  3 2
#3+2=5
#3-2=1
#3*2=6
#3/2=1
a,b = map(int,input().split())
print("%d+%d=%d" % (a,b,a+b))
print("%d-%d=%d" % (a,b,a-b))
print("%d*%d=%d" % (a,b,a*b))
print("%d/%d=%d" % (a,b,a/b))

#1117
#두 실수를 입력받아 두 실수의 곱을 출력하되 소수 둘째자리까지 출력하시오.
a,b = map(float,input().split())
print("%.2f" % (a*b))

#1118
#삼각형의 넓이를 구하는 프로그램을 작성한다.
#삼각형의 넓이 = 밑변 * 높이 / 2
a,b = map(int,input().split())
print(a*b/2)

#1119
#하루는 24시간이다.
#일(day)이 입력으로 주어지면 시간으로 변환하시오.
a = int(input())
print(a*24)

#1120
#세 정수가 입력되면 평균을 출력하시오.
a,b,c = map(int,input().split())
print("%.2f"% ((a+b+c)/3))