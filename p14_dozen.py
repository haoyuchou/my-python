x = int(input())
n = x//12
y = x%12
if y==0:
    print(n,'dozen')
else:
    print(n, 'dozen and', y)
