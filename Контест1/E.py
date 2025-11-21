n, m = map(int, input().split())
a=[]
dp=[]

for i in range (n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    h=[]
    for _ in range(m):
        w=[-10**9,-10**9,-10**9]
        h.append(w)
    dp.append(h)

dp[0][0][1]=a[0][0]
dp[0][0][2]=a[0][0]
dp[0][0][0]=a[0][0]

for i in range (n):
    for j in range (m):
        for k in range (3):
            if k!=1 and i<n-1:
                dp[i+1][j][1]=max(dp[i+1][j][1],dp[i][j][k]+a[i+1][j])
            if k!=2 and j<m-1:
                dp[i][j+1][2]=max(dp[i][j+1][2],dp[i][j][k]+a[i][j+1])
            if k!=0 and i<n-1 and j<m-1:
                dp[i+1][j+1][0]=max(dp[i+1][j+1][0],dp[i][j][k]+a[i+1][j+1])

print(max(dp[n-1][m-1][1],dp[n-1][m-1][2],dp[n-1][m-1][0]))


'''
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][k] — максимум алмазов в (i,j), если пришли направлением k
# k = 0 (вниз), 1 (вправо), 2 (диагональ)
dp = [[[-10**9]*3 for _ in range(m)] for _ in range(n)]

# Стартовая позиция
for k in range(3):
    dp[0][0][k] = a[0][0]

for i in range(n):
    for j in range(m):
        for k in range(3):  # последнее направление
            if dp[i][j][k] == -10**9:
                continue
            # движение вниз
            if i+1 < n and k != 0:
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][k] + a[i+1][j])
            # движение вправо
            if j+1 < m and k != 1:
                dp[i][j+1][1] = max(dp[i][j+1][1], dp[i][j][k] + a[i][j+1])
            # движение по диагонали
            if i+1 < n and j+1 < m and k != 2:
                dp[i+1][j+1][2] = max(dp[i+1][j+1][2], dp[i][j][k] + a[i+1][j+1])

# Результат — максимум из трёх направлений в правом нижнем углу
print(max(dp[n-1][m-1]))

'''
