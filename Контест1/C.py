n=int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
        for j in range(0, i):
            ...
        for j in range(i, n + 1):
            ...
    return dp[n][n]