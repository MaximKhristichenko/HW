A=input()
a=list(A)
s=[]
for i in range (len(a)):
    if a[i]=="(" or a[i]=="[" or a[i]=="{":
        s.append(a[i])
    elif a[i]==")" or a[i]=="]" or a[i]=="}":
        if len(s)==0:
            print("No")
            break
        if a[i]==")" and s[-1]== "(":
            s.pop(-1)
        elif a[i]=="]" and s[-1]== "[":
            s.pop(-1)
        elif a[i]=="}" and s[-1]== "{":
            s.pop(-1)
        else:
            print('No')
            break
    else:
        print("No")
        break
else:
    if len(s)==0:
        print('Yes')
    else:
        print('No')
