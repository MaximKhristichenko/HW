def mnk(x,y):
    if len(x)!=len(y):
        raise ValueError("number of x and y values must be the same")
    l=len(x)
    if l==0 or l==1:
        raise ValueError("number of x and y values must be 2 or more")
    sumxx=0
    sumxy=0
    sumx=sum(x)
    sumy=sum(y)
    for j in range(0,l):
        assert type(x[j]) is float, "x must be float type"
        assert type(y[j]) is float, "y must be float type"
        sumxy+=x[j]*y[j]
    for i in range(0,l):
        sumxx+=x[i]*x[i]
    d=sumxx-sumx*sumx/l
    if d==0:
        raise ValueError("x values must be different")
    a=((sumxy-sumx*sumy/l)/d)
    b=sumy/l-a*sumx/l
    return a, b

if __name__ == "__main__":
    x=list(map(float, input("enter x values separated by spaces ").split()))
    y=list(map(float, input("enter y values separated by spaces ").split()))
    print(mnk(x,y))