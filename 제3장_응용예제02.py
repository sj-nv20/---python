#Python for Beginner 제3장_응용예제02

#입력 문자열을 거꾸로 출력하기
#문자열을 입력받고, 입력받은 문자열의 순서를 거꾸로 출력해 보자

## 변수 선언 부분 ##
inStr = ' '

## 메인 코드 부분 ##
if __name__ == "__main__" :
    inStr = input("문자열을 입력 -->")

    for i in range(len(inStr)-1, -1, -1) :
        print('%c' % inStr[i], end='')