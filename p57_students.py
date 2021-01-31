class student:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        self.grades=[]

    def avg(self):
        return sum(self.grades)/len(self.grades)
    def add(self,score):
        self.grades.append(score)
    def fcount(self):
        fct=0
        for i in self.grades:
            if i<60:
                fct+=1
        return fct
    def show(self):
        print('Name:',self.name)
        print('Gender:',self.gender)
        print('Grades:',self.grades)
        print('Avg:',self.avg())
        print('Fail Number:',self.fcount())
def top(*students):
    maxvalue=0
    maxi=0
    for i in students:
        if i.avg()>maxvalue:
            maxvalue=i.avg()
            maxi=i
    return maxi.show()        
                
        
           
            
   
s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)
 

s1.show()
print()

s2.show()
print()

s3.show()
print()

s4.show()
print()

s5.show()
print()
print('Top Student:')
top_student = top(s1,s2,s3,s4,s5)
print()


            
