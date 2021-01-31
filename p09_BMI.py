x = eval(input())
y = eval(input())
a = y/(x*x/100/100)
a*=100
#四捨五入
add = a*10
if add%10 >= 5:
    a += 1
#去掉餘數
a//=1
a/=100
if a<18.5:
    print(a)
    print('Underweight')
elif a>=18.5 and a<24:
    print(a)
    print('Normal')
elif a>=24 and a<27:
    print(a)
    print('Overweight')
elif a>=27 and a<30:
    print(a)
    print('Obese Class Ⅰ')
elif a>=30 and a<35:
    print(a)
    print('Obese Class II')
else:
    print(a)
    print('Obese Class III')
    
    
        
    
