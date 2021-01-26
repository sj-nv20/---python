# 1021
# 1개의 단어를 입력받아 그대로 출력해보자.
a = input()
print(a)

# 1022
# 공백 문자가 포함되어 있는 문장을 입력받고 그대로 출력하는 연습을 해보자.
b = input()
print(b)

# 1023
# 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
a,b = input().split('.')
print(a)
print(b)

# 1024**
# 단어를 1개 입력받는다. 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.
a = input()
for i in a:
    print("'" + i + "'")

# 1025**
# 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
a = input()
list = []
for i in a:
    list.append(i)

print('[{0}]'.format(int(list[0]) * 10000))
print('[{0}]'.format(int(list[1]) * 1000))
print('[{0}]'.format(int(list[2]) * 100))
print('[{0}]'.format(int(list[3]) * 10))
print('[{0}]'.format(int(list[4])))

#1026
#입력되는 시:분:초 에서 분만 출력해보자.
a,b,c = input().split(":")
print(int(b))

#1027**
#년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다. 년월일(yyyy.mm.dd)를 입력받아, 일월년(dd-mm-yyyy)로 출력해보자.
a,b,c = input().split('.')
print("%02d" % int(c), end = '-')
print("%02d" % int(b), end = '-')
print("%04d" % int(a))

#1028
# 정수 1개를 입력받아 그대로 출력해보자. (단, 입력되는 정수의 범위는 0 ~ 4,294,967,295 이다.)
a = int(input())
print(a)

#1029
#실수 1개를 입력받아 그대로 출력해보자.(단, 입력되는 실수의 범위는 +- 1.7*10-308 ~ +- 1.7*10308 이다.)
a = float(input())
print("%.11f" % a)

#1030
#정수 1개를 입력받아 그대로 출력해보자.단, 입력되는 정수의 범위는 -9,223,372,036,854,775,808 ~ +9,223,372,036,854,775,807 이다.
a = int(input())
print(a)