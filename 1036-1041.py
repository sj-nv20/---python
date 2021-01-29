#1036
#영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
a = input()
a1 = ord(a) # ord = 아스키코드 값으로 변환해주는 함수
print(a1)

#1037
#10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
a = input()
a1 = int(a)
a2 = chr(a1)    # chr = 아스키코드값을 문자로 변환해주는 함수
print(a2)

#1038
#정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
a,b = input().split()
print(int(a)+int(b))

#1039
#정수 2개를 입력받아 합을 출력해보자.
a,b = input().split()
print(int(a)+int(b))

#1040
#입력된 정수의 부호를 바꿔 출력해보자.
a = int(input())
print("%d" % -a)

#1041
#영문자 1개를 입력받아 그 다음 문자를 출력해보자.
a = input()
a1 = ord(a)
a2 = chr(a1+1)
print(a2)