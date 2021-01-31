f1 = open('../app/stores_old.csv','r',encoding='big5')
txtLst = f1.readlines()
f1.close()
x= 'Y'
for i in range(len(txtLst)):
    for j in range(len(txtLst[i])):
        if x in txtLst[i][j]:
            print(txtLst[i],end='')
           
