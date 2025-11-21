def h(s):
    h = 0
    p = 1
    for c in reversed(s):
        h = (h + ord(c) * p) % 100
        p = (p * 91) % 100
    return h

t = [[] for _ in range(10)]

for _ in range(int(input())):
    k, v = input().split()
    x = h(k)
    i = x % 10
    for e in t[i]:
        if e[1] == k:
            e[2] = v
            break
    else:
        t[i].append([x, k, v])

for i, c in enumerate(t):
    if c:
        print(i)
        for e in c:
            print(e[0], e[1], e[2])