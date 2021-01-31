class pokemon:
    pct=0

    def __init__(self,Name,Lv,Hp,HpMax):
        self.Name=Name
        self.Lv=Lv
        self.Hp=Hp
        self.HpMax=HpMax
        pokemon.pct+=1
    def attack(self,target):
        if (target.Hp<=0):
            print('對方',target.Name,'不可被攻擊')
            return
        if (self.Hp<=0):
            print('己方',self.Name,'已失去戰鬥力')
            return
        print(self.Name,'攻擊了',target.Name,self.Lv)
        target.defense(self.Lv)
        

    def defense(self,damage):
        self.Hp-=damage
        if self.Hp<=0:
            self.Hp=0
            print(self.Name,'已失去戰鬥力')
        

    def cure(self):
        print(self.Name,'已恢復戰鬥力')
        self.Hp=self.HpMax

    def showInfo(self):
        #print('pokemon Data')
        print('Name:',self.Name)
        print('Lv:',self.Lv)
        print('Hp:%d/%d'%(self.Hp,self.HpMax))

p1=pokemon('妙蛙種子',100,200,200)
p1.showInfo()
p2=pokemon('可達鴨',50,100,100)
p2.showInfo()
p1.attack(p2)
p2.showInfo()
