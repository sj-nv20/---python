#Python for Beginner 제4장_02[프로그램1]

# 학습한 연산자를 활용해서 동전 교환 프로그램을 구현해보자.

## 변수 선언 부분##
money, c500, c100, c50, c10 = 0,0,0,0,0

## 메인 코드 부분 ##
money = int(input("교환할 돈은 얼마?"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n 500원 짜리 ==> %d개" % c500)
print("\n 100원 짜리 ==> %d개" % c100)
print("\n 50원 짜리 ==> %d개" % c50)
print("\n 10원 짜리 ==> %d개" % c10)
print("\n 바꾸지 못한 잔돈 ==> %d원 \n" % money)