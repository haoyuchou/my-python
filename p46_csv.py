f1 = open('../app/stores_old.csv','r',encoding='big5')
txtLst = f1.readlines()
f1.close()

for i in range(len(txtLst)):
    txtLst[i]=txtLst[i].strip()
    print(txtLst[i])
