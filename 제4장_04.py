#Python for Beginner 제4장_04

#논리 연산자


##논리 연산자의 종류와 사용
'''
and(그리고)     ~이고, 그리고       둘 다 참이어야 참           (a>100)and(a<200)
or(또는)        ~이거나, 또는       둘 중 하나만 참이어도 참    (a==100)or(a==200)
not(부정)       ~아니다, 부정       참이면 거짓, 거짓이면 참    not(a<100)
'''

a = 99
print((a>100)and(a<200))    #False
print((a>100)or(a<200))     #True
print(not(a==100))          #True

##Python은 숫자도 참 거짓으로 구분 - 0(거짓), 0외의 값(참)

