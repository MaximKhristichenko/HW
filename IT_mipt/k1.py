def f(n,m):
    if n%2==0 or m%2==0:
        return 0
    return 1+4*f(n//2, m//2)


a, b =map(int, input().split())
print(f(a,b))