x = eval(input())

if x >= 95:
    print('獎金 2000 元')
elif x >= 90 and x <= 94:
    print('獎金 1000 元')
elif x >= 80 and x <= 90:
    print('獎金 500 元')
else:
    print('獎金 0 元')
