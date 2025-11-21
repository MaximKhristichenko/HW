import heapq
n=int(input())
h=[]
ans=[]
heapq.heapify(ans)
sumtime=0
for _ in range (n):
    t,d=map(int,input().split())
    h.append(((-1)*t,d))
h.sort(key=lambda x: x[1])

for y,d in h:
    heapq.heappush(ans, y)
    sumtime+=y
    if (-1)*sumtime>d:
        a=heapq.heappop(ans)
        sumtime-=a
print(len(ans))