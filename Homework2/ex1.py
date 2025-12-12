def prime(a):
    assert type(a) is int, "number must be integer"
    assert a>=0, "number must be positive"
    if a==1:
        raise ValueError("number 1 has no prime divisors")
    return prime1(a)

def prime1(a, d=2):
    if a==1:
        return []
    if a%d==0:
        return [d] + prime1(a//d,d)
    if a<d**2:
        return [a]
    else:
        return prime1(a,d+1)
    
if __name__ == "__main__":
    a=int(input())
    print(prime(a))
