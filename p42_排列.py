def fact(x):
    total=1
    for i in range(1,x+1):
        total*=i
    return total

def P(n,m):
    return fact(n)/fact(n-m)
a=int(input())
b=int(input())
print(round(P(a,b)))
    
