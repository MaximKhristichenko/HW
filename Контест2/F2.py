import heapq
p=list(map(int,input().split()))
h1=[]
h2=[]
m=0
def roundtwo(a):
    if a//2==a/2:
        return a//2
    if a//2<a/2:
        return a//2+1

print(p[0], end=' ')
if p[0]<=p[1]:
    heapq.heappush(h1, -p[0])
    heapq.heappush(h2, p[1])
elif p[0]>p[1]:
    heapq.heappush(h1, -p[1])
    heapq.heappush(h2, p[0])
print(roundtwo(-h1[0]+h2[0]), end=' ')

for i in range(2, len(p)):
    if p[i]>=h2[0]:
        heapq.heappush(h2, p[i])
    else:
        heapq.heappush(h1, -p[i])

    if len(h1)>len(h2):
        a=-heapq.heappop(h1)
        heapq.heappush(h2, a)
    elif len(h2)>len(h1)+1:
        a=heapq.heappop(h2)
        heapq.heappush(h1, -a)

    if len(h1)==len(h2):
        print(roundtwo(-h1[0]+h2[0]), end=' ')
    else:
        print(h2[0], end=' ')


'''
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
'''