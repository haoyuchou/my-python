def fact(n):
    total = 1
    for i in range(1,n+1):
        total*=i
    return total

x=eval(input())
print(fact(x))
