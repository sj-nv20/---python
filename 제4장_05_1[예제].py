#Python for Beginner 제4장_05_1[예제]

#비트 연산을 활용할 수 있는 예제


##ord()함수 => 글자를 아스키 코드값으로 변경시켜준다
##아스키코드값이란? 
##영문 대문자 A는 65, B는 66, C는 67등으로 할당되어 있고 영소문자는 a는 97, b는 98등으로 할당되어 있음

a = ord('A')
mask = 0x0F         # [2진수] 0 0 0 0   1 1 1 1

print("%x & %x = %x" % (a, mask, a&mask))   #41 & f = 1
print("%x | %x = %x" % (a, mask, a|mask))   #41 | f = 4f

mask = ord('a') - ord('A')

b = a ^ mask
print("%c ^ %d = %c" % (a, mask, b))        #A ^ 32 = a
a = b ^ mask
print("%c ^ %d = %c" % (b, mask, a))        #a ^ 32 = A
