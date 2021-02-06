# 1096
# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
n=int(input())
a=[[0 for j in range(20)] for i in range(20)]
for i in range(n):
    x,y=list(map(int,(input().split())))
    a[x][y]=1    
for j in range(1,20):
    for k in range(1,20):
        print(a[j][k],end=' ')
    print('')

# 1097
# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
a=[[0 for j in range(20)] for i in range(20)]
for k in range(19):
    x=list(map(int,(input().split())))
    for l in range(19):
        a[k+1][l+1]=x[l]
n=int(input())
for v in range(n):
    v1,v2=map(int,(input().split()))
    for m in range(1,20):
        if a[v1][m]==0:
            a[v1][m]=1
        else:
            a[v1][m]=0
        if a[m][v2]==0:
            a[m][v2]=1
        else:
            a[m][v2]=0
for o in range(1,20):
    for p in range(1,20):
        print(a[o][p],end=' ')
    print('') 

# 1098
# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
h,w=map(int,(input().split()))
a=[[0 for j in range(w+1)]for i in range(h+1)]
n=int(input())
for k in range(n):
    l,d,x,y=map(int,(input().split()))
    for m in range(l):
        if d==0:
            a[x][y+m]=1
        else:
            a[x+m][y]=1
for o in range(1,h+1):
    for p in range(1,w+1):
        print(a[o][p],end=' ')
    print('')  
# 1099
# 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.
# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
# 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.
# 미로 상자의 테두리는 모두 벽으로 되어 있으며,
# 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
m=[] 
for i in range(12) :
     m.append([]) 
     for j in range(12) :
        m[i].append(0) 
        
for i in range(10) : 
    a=input().split() 
    for j in range(10) : 
        m[i+1][j+1]=int(a[j]) 
x=2
y=2 
while True : 
    if m[x][y]==0 : 
        m[x][y]=9 
    elif m[x][y]==2 : 
        m[x][y]=9 
        break 
    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) : 
        break 
    if m[x][y+1]!=1 : 
        y+=1 
    elif m[x+1][y]!=1 : 
        x +=1 

for i in range(1, 11) : 
    for j in range(1, 11) : 
        print(m[i][j], end=' ') 
    print()

