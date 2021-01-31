def sum1(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total

x=eval(input())
print(sum1(x))
