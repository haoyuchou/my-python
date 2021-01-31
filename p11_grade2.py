x=eval(input())
if x==1 or x==2:
    y=eval(input())
    if (x==1 and 100>=y>=60) or (x==2 and 100>=y>=70):
        print('pass')
    elif y>100 or y <0:
        print('score error')
    else:
        print('fail')
else:
    print('roll error')
        
