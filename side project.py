class naruto():
    def __init__(self,name,hp,maxhp,lv,chakra,maxchakra):
        self.name=name
        self.hp=hp
        self.maxhp=maxhp
        self.lv=lv
        self.chakra=chakra
        self.maxchakra=maxchakra
        self.substitute=4
    def normalattack(self,target): #普攻
        import random
        if target.hp>0 and self.chakra>=2:
            
            self.chakra-=2
            print(self.name,'施放了普攻')
            if random.randrange(1,6)>=1:
                target.defense()
            else:
                target.dodgenormalattack()
        if target.hp<0:
            print('遊戲結束')
            return
        
    def defense(self):
        import random #普攻防禦
        if random.randrange(1,101,1)>80:
            
            print(self.name,'防禦成功')
        elif random.randrange(1,101,1)<=80 and self.hp>=2:
            self.hp-=2
            print(self.name,'防禦失敗')
        elif random.randrange(1,101,1)<=80 and self.hp<2:
            self.hp-=2
            print(self.name,'防禦失敗,遊戲結束')
            return
            


    def powermove(self,target): #大絕
        if self.chakra<self.maxchakra*0.8:
            return
        if self.chakra>=self.maxchakra*0.8:
            self.chakra-=self.maxchakra*0.8
            if target.hp>=self.lv/2:
                target.hp-=(self.lv/2)
            if target.hp<self.lv/2:
                target.hp-=target.hp
            print(self.name,'施放大招')
            target.dodge(self)    
    def dodgenormalattack(self):#替身閃躲普攻
         if self.substitute>0:
                self.substitute-=1
                print(self.name,'閃躲成功')
    def dodge(self,enemy): #替身閃躲大絕
        import time
        import random
        starttime=time.time()
        
       
        
        if self.substitute>0 and self.hp>enemy.lv/2:
            if random.randrange(1,3)==1:
                self.substitute-=1
                self.hp+=enemy.lv/2
                print(self.name,'閃躲成功')
        elif self.substitute>0 and self.hp<=enemy.lv/2:
            if random.randrange(1,3)==1:
                self.substitute-=1
                self.hp+=self.hp
                print(self.name,'閃躲成功')
        elif self.substitute==0 and self.hp<=enemy.lv/2:
            print('遊戲結束')
            return
        while self.substitute<=3:
            if time.time()-starttime>=20:
                self.substitute+=1
    def chakraback(self): #查克拉恢復
        import time
        inter=time.time()
        if self.chakra+2<=self.maxchakra and time.time()-inter>=2:
             self.chakra+=2
             print(self.name,'查克拉恢復')
             return
        if self.chakra+2>self.maxchakra and time.time()-inter>=2:
             self.chakra=self.maxchakra
             print(self.name,'查克拉恢復')
             return
    
        
            
            
            
             
        
        
    def showresult(self):
        print('name:',self.name)
        print('hp:',self.hp)
        print('lv',self.lv)
        print('chakra:',self.chakra)
        print('substitute:',self.substitute)
def battle(x,y): #對戰
    
    import random
    import time
    
    begin=time.time()
    while True:
        x.chakraback()
        y.chakraback()
        if random.randrange(1,101,1)<80:
            x.normalattack(y)
            
            
        if random.randrange(1,101,1)<80:
            y.normalattack(x)
            
        if random.randrange(1,101,1)>50:
            x.powermove(y)
           
        if random.randrange(1,101,1)>50:
            y.powermove(x)
        if time.time()-begin>=90:
            print ('game over')
            if x.hp>y.hp:
                print(x.name,'獲勝了')
            else:
                print(y.name,'獲勝了')
            return x.showresult(), y.showresult() 
            break
        if x.hp<0 or y.hp<0:
            print('game over')
            if x.hp>y.hp:
                print(x.name,'獲勝了')
            else:
                print(y.name,'獲勝了')
            return x.showresult(), y.showresult() 
            break
    #return x.showresult(), y.showresult()    

s1=naruto('漩渦鳴人',20,20,10,30,30)
s2=naruto('宇志波佐助',15,15,9,20,20)
s3=naruto('旗木卡卡西',15,15,10,25,25)
s4=naruto('自來也',16,16,9,28,28)

    
battle(s3,s4)

        
        

    
        
                
            
