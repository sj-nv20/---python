#Python for Beginner 제4장_05_2[예제]

a = 100
result = 0
i = 0

for i in range(1,5) :
    result = a << i
    print("%d << %d = %d" % (a, i, result))

print("-------------------")

for i in range(1,5) :
    result = a >> i
    print("%d >> %d = %d" % (a, i, result))

'''
결과    
100 << 1 = 200
100 << 2 = 400
100 << 3 = 800
100 << 4 = 1600
-----------------
100 >> 1 = 50
100 >> 2 = 25
100 >> 3 = 12
100 >> 4 = 6
'''