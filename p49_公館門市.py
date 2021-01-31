f1 = open('../app/stores_old.csv','r',encoding='big5')
txtLst = f1.readlines()
f1.close()
x= '公館門市'
for i in range(len(txtLst)):
    if x in txtLst[i]:
        print(txtLst[i],end='')
        break
