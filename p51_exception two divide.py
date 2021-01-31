while True:
    try:
        a = eval(input())
        b = int(input())
        c = a/b
    except NameError:
        print('NameError')
    except ValueError:
        print('ValueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    else:
        print("%d/%d = %.2f"%(a,b,a/b))
        break
