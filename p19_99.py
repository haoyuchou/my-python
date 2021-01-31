n=eval(input())
for j in range(1,n):
    for i in range(1,n):
        print(i,'*',j,'=',i*j,end='\t',sep='')
    print()
