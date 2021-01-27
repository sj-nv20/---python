# 1031
# 10진수를 입력받아 8진수(octal)로 출력해보자.
a = input()
print("%o" % int(a))

# 1032
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
a = input()
print("%x" % int(a))

# 1033
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
a = input()
print("%X" % int(a))

# 1034
# 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
a = input()
a1 = int(a, 8)
print(a1)

# 1035
# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
a = input()
a1 = int(a, 16)
print("%o" % a1)