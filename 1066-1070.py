#1066
#세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
a,b,c = map(int,input().split())
if a%2 == 0 :
    print("even")
else :
    print("odd")
if b%2 == 0 :
    print("even")
else :
    print("odd")
if c%2 == 0 :
    print("even")
else :
    print("odd")

#1067
#정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
a = int(input())
if a > 0 :
    print("plus")
    if a % 2 == 0 :
        print("even")
    else :
        print("odd")
else :
    print("minus")
    if a % 2 == 0 :
        print("even")
    else :
        print("odd")
        
#1068
#점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
a = int(input())
if a >= 90 :
    print("A")
elif a >= 70 :
    print("B")
elif a >= 40 :
    print("C")
else :
    print("D") 

#1069
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
a = input()
if a == "A" :
    print("best!!!")
elif a == "B" :
    print("good!!")
elif a == "C" :
    print("run!")
elif a == "D" :
    print("slowly~")
else :
    print("what?")

#1070
#월이 입력될 때 계절 이름이 출력되도록 해보자.
a = int(input())
a1 = [1,12,2]
a2 = [3,4,5]
a3 = [6,7,8]
a4 = [9,10,11]
if a in a1 :
    print("winter")
elif a in a2 :
    print("spring")
elif a in a3 :
    print("summer")
elif a in a4 :
    print("fall")