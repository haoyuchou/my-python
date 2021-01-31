m = eval(input())
for m in range(2,m+1):
    fct=0
    for i in range(1,m+1):
        if m%i==0:
            fct+=1
    if fct==2:
        print(m,'is prime')
