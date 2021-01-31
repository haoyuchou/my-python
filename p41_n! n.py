def return2num(n=0):
    total=0
    for i in range(1,n+1):
        total+=i
    total2=1
    for i in range(1,n+1):
        total2*=i
    return total2,total
x=int(input())
ans=return2num(x)
print(ans[0])
print(ans[1])
