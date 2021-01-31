n=eval(input())
lst=[]
for i in range(n,1-1,-1):
    lst.append(i)
    print('data',i)

print()    
for i in range(len(lst)):
    print('data',lst.pop())
