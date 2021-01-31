from random import sample
from time import sleep



for i in range(3,1-1,-1):
    print(i)
    sleep(i)
res=sample(range(1,49+1,1),7)
print('lot:',res[:6])
print('sp:',res[6])
