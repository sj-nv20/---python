#1081**
#1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.
n, m = map(int,input().split())
for x in range(1, n+1, 1):
    for k in range(1, m+1, 1):
        print("%d %d" % (x,k))

#1082**
#16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운 영일(01)이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.
#A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
a = str(input())    #str - 문자열 
b = int(a,16)
for x in range(1,16):
        print("%s*%X=%X" % (a,x,b*x))   # %s = 문자열 / %X = 16진수
        
#1083
#3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다. 3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.
a = int(input())
for x in range (1,a+1,1):
    if x % 3 == 0:
        print("X")
    else :
        print(x)

#1084**
#빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 빛의 색을 만들어 내려고 한다.
#빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때, (빛의 강약에 따라 0 ~ n-1 까지 n가지의 빛 색깔을 만들 수 있다.)
#주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과 총 가짓 수를 계산해보자.
r,g,b = map(int,input().split())
num = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            num +=1
print(num)
