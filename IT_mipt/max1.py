a=int(input())
b=int(input())
c=int(input())
if a==0 or b==0 or c==0:
    print('impossible')
elif a>=b+c or b>=a+c or c>=b+a:
    print('impossible')
elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
    print('right')
elif a**2<b**2+c**2 and b**2<a**2+c**2 and c**2<a**2+b**2:
    print('acute')
elif a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2:
    print('obtuse')
else:
    print('impossible')