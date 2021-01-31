a=eval(input())
total = 0
for b in range(1,a+1):
    total += b #total = total + b
    print(b,end='')
    if (b!=a):
        print('+', end='')
print(' =',total)    
