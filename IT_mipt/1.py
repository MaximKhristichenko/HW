s = input().strip()
num = ''
res = 1
for ch in s:
    if ch.isdigit():
        num += ch
    else:
        if num:
            res *= int(num)
            num = ''
if num:
    res *= int(num)
print(res)**