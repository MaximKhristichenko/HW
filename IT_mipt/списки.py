a=list(map(int,input().split()))
n=int(input())

def reverse_array(a, n):
    b=a[n-1::-1]
    c=a[n::]
    b.extend(c)
    return (b)

print(reverse_array(a, n))
