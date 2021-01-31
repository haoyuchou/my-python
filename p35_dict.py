d={'P':'Pikachu', 'M':'Mickey Mouse', 'H':'Hello kitty'}

while True:
    keyin = input()
    if keyin =='-1':
        break
    if keyin in d:
        print(d[keyin])
    else:
        print(keyin, 'does not exist. Enter a new one:')
        ndata = input()
        d[keyin] = ndata
