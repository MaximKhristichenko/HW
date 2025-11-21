def fdp(n,m,x,y):
    r=[0]
    r.extend(x)
    p=[0]
    p.extend(y)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range (1, n+1):
        for j in range (1, m+1):
            if r[i]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-r[i]]+p[i])
    return dp[n][m]


N, M = map(int, input().split())
x=list(map(int, input().split()))
y=list(map(int, input().split()))
print(fdp(N,M,x,y))