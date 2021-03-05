#Python for Beginner 제3장_응용예제01

#데이터형 크기 확인하기
#파이썬에서 제공되는 각 데이터형의 기본 크기를 확인하는 프로그램

import sys      # 데이터형 크기를 확인하는 sys.getsizeof()함수를 사용하려고 sys를 임포트

## 변수 선언 부분 ##
intVar, floatVar, strVar, boolVar, listVar, tupleVar, dictVar, setVar = [None] * 8      #데이터형 확인한느 전역변수 8개 선언 / [None] * 8은 None을 8개 쓴것과 같은 효과

## 메인 코드 부분 ##
if __name__ == "__main__" :
    intVar = 0
    floatVar = 0.0
    strVar = ""
    boolVar = True
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print('int형 기본 크기 -->', sys.getsizeof(intVar))
    print('float형 기본 크기 -->', sys.getsizeof(floatVar))
    print('str형 기본 크기 -->', sys.getsizeof(strVar))
    print('bool형 기본 크기 -->', sys.getsizeof(boolVar))
    print('list형 기본 크기 -->', sys.getsizeof(listVar))
    print('tuple형 기본 크기 -->', sys.getsizeof(tupleVar))
    print('dict형 기본 크기 -->', sys.getsizeof(dictVar))
    print('set형 기본 크기 -->', sys.getsizeof(setVar))
