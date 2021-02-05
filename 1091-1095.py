
#1091**
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
# n번째 수를 출력하는 프로그램을 만들어보자.
a,m,d,n = map(int,input().split())
for x in range(n-1) :
    a = a*m+d
print(a)

#1092***
# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
# 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
a,b,c = map(int,input().split())
day=1;
while(day%a!=0 or day%b!=0 or day%c!=0) :
    day += 1;
print(day);

#1093***
# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
n = int(input())
num = input().split()
result = [0 for i in range(24)]

for i in range(n):
    result[int(num[i])] += 1

for i in range(1,24):
    print(result[i], end=' ')

#1094
# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.
n = int(input())
num = input().split()
li_num = list(num)
result = []

for i in range(n):
    result.append(li_num[i])
print(' '.join(reversed(result)))

# 1095
# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
n = int(input())
num = input().split()
li_num = list(num)
result = []

for i in range(n):
    result.append(int(li_num[i]))
print(min(result))