#Python for Beginner 제3장_03

#변수의 선언과 사용


#변수의 선언

#변수선언 => 그릇을 준비하는 것
#변수의 종류 - 불형(Boolean, True 또는 False저장), 정수형, 실수형, 문자열
boolVar = True      #불형
intVar = 0          #정수형
floatVar = 0.0      #실수형
strVar = ""         #문자열
# boolVar , intVar, floatVar, strVar = True, 0, 0.0, ""  - 이러한 표현도 가능

#변수명 규칙
# 1. 대소문자 구분
# 2. 문자, 숫자, _ 포함가능 하지만 숫자로 시작은 불가능하다
# 3. 예약어는 변수로 사용 불가능
# 예약어 => True, False, None, and, or, not, break, continue, return, if, else, elif,
#           for, while, except, finally, gloval, import, try등
# type()함수를 사용하면 변수의 형태를 확인할 수 있음

print(type(boolVar), type(intVar), type(floatVar), type(strVar))       
#(<class 'bool'>, <class 'int'>, <class 'float'>, <class 'str'>)

#변수의 사용
#변수는 입력값을 새로 받을 경우 기존 값은 없어진다

var2 = 200
var1 = var2
print(var1) #200

var1 = 100+100
print(var1) #200

var1 = var2+100
print(var1) #300

var1 = var2 = var3 = var4 = 100
# 또는
var4 = 100
var3 = var4
var2 = var3
var1 = var2

var1 = var1 + 200   
print(var1)     #300

# NameError: name 'noVar' is not defined 오류 발생할 경우

noVar = noVar + 200
print(noVar)        #오류발생

#noVar = 0 등의 형태로 noVar에 값을 대입시켜 둬야함
noVar = 0
noVar = noVar + 200
print(noVar)   #200

#파이썬은 변수 선언 없이 사용 가능
#한 번 선언된 변수는 다른 타입을 넣어도 됨 - 다른타입을 넣는 순간 변수의 형도 변경되기때문 => 유연한 구조
myVar = 100         #정수형
print(type(myVar))         #<class 'int'>
myVar = 100.0       #실수형
print(type(myVar))         #<class 'float'>

# 변수는 =를 기준으로 모두 왼쪽에 위치하여야한다.

10 = 100    #오류 = 변수가 없기 때문
100 = a     #오류 = 변수가 왼쪽에 있기 때문에
a = 100
print(a)    # 100