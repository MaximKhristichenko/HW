n = int(input())
a = str(input())
if a == 'monkey':
    x=n//90
if a == 'parrot':
    x=n//10
if a == 'elephant':
    x=n//300
if x==0:
    x=1
print(x)