A, M =map(int, input().split())
S=input().strip()

def f(b,m,s):
    n=0
    p=1
    for i in reversed (s):
        n=(n+ord(i)*p)%m
        p=p*b
    return n

print(f(A,M,S))