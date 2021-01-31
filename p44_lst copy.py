
lst=[]
while True:
    n=eval(input())
    if n==-1:
        break
    lst.append(n)

def Find3rdMax(lst):
    lst.sort()
    print('sorted =',lst)
    return lst[-3]

print('input =',lst)
print('max 3rd =',Find3rdMax(lst.copy()))
print('list =',lst)
