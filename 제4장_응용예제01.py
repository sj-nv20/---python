#Python for Beginner 제4장_응용예제01

#윤년 계산기


#입력된 연도가 윤년인지 계산하는 프로그램
#4로 나누어 떨어지고, 100으로 나누어 떨어지지 않으면 윤년이다.
#400으로 나누어 떨어지는 해도 윤년에 포함된다.

## 전역 변수 부분 ##
year = 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
    year = int(input("연도를 입력하세요 : "))

    if((year % 4 == 0 ) and (year % 100 != 0)) or (year % 400 == 0) :
        print("%d는 윤년입니다." % year);
    else:
        print("%d는 윤년이 아닙니다." % year);