def f(x,n,m):
    if (n+x)%m==0 and (m+x)%n==0:
        return x
    return f(x+1,n,m)

a, b = map(int, input().split())
print(f(0,a,b))