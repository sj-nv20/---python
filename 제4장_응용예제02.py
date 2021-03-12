#Python for Beginner 제4장_응용예제02

#거북이로 2진수 숫자 표현하기


#입력한 10진수를 2진수 변환해 거북이로 표현하는 프로그램
#10진수 5를 입력하면 거북이로 2진수 101을 표현하기
#1은 빨간색 거북이로 크기를 두배 출력하고 0은 파란색 거북이로 크기를 기본으로 출력

import turtle

## 전역 변수 부분 ##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num = int(input("숫자를 입력하세요 : "))
    binary = bin(num)
    curX = swidth / 2
    curY = 0
    for i in range(len(binary) - 2) :
        turtle.goto(curX, curY)
        if num & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1
        
turtle.done()