x = int(input())
y = int(input())
for i in range(1,x+1):
    for b in range(1,y+1):
         print("%d*%d=%2d"%(i,b,i*b),end=' ')
    print()
        
