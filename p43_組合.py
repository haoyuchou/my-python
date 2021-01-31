def fact(x):
    total=1
    for i in range(1,x+1):
        total*=i
    return total

def C(n,m):
    return fact(n)/fact(m)/fact(n-m)
a=int(input())
b=int(input())
print(round(C(a,b)))
    
