math={'柯南', '灰原', '步美', '美環', '光彦'}
english={'柯南', '灰原', '丸尾', '野口', '步美'}
x = math.union(english)
y = math.intersection(english)
r=math-english
lst1=list(r)
lst1.sort()
print(lst1)
t=english-math
lst2=list(t)
lst2.sort()
print(lst2)
lst3=list(y)
lst3.sort()
print(lst3)
