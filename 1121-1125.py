#1121
#정수 계산에서 나머지를 구하시오.
a,b = map(int,input().split())
print("%d" % (a%b))

#1122
#초를 입력받아 분 / 초의 형태로 출력하시오.
a = int(input())
m = int(a/60)
c = int(a%60)
print("%d %d" % (m,c))

#1123
#섭씨 온도가 입력되면 화씨 온도로 변환하시오.
a = int(input())
b = (9/5*a+32)
print("%.3f" % b)

#1124**
#화학 숙제를 하던 광곽이는 분자량을 구하라는 문제를 보고 귀찮아 한다.
#귀찮은 광곽이를 위해서 화학식을 입력하면 분자량을 구해주는 프로그램을 만들어 주자!
#화학식은 CxHy의 꼴로 입력된다.
#C의 원자량은 12, H의 원자량은 1로 한다.
a,b = input().split("H")
c = int(a[1:])  
b = int(b)
print(12*c+b) 

#1125
#10진수 정수를 입력받아 8진수와 16진수로 출력한다.
a = int(input())
print("%o %X" % (a,a))