import os
N=eval(input())

if os.path.exists('files'):
    os.chdir('files')
    for i in os.listdir():
        os.rmdir(i)
    os.chdir('../')
    os.rmdir('files')
os.mkdir('files')
os.chdir('files')
for i in range(1,N+1):
    os.mkdir('f'+str(i))
x=os.listdir()
x.sort()
print(x)    
os.rename('f1','folder1')
y=os.listdir()
y.sort()
print(y)
os.rmdir('folder1')
z=os.listdir()
z.sort()
print(z)
os.chdir('../')
os.chdir('files')
for i in os.listdir():
    os.rmdir(i)
os.chdir('../')
os.rmdir('files')
