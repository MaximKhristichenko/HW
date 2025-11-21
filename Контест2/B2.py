N=int(input())
s=[]
d=-1000000
n=0
for _ in range (N):
    l,r=map(int,input().split())
    s.append((l,r))
s.sort(key=lambda x: x[1])
for l,r in s:
    if l>d:
        d=r
        n+=1
print(n)
