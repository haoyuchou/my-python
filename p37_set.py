itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}# 這是第一個集合 
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}  # 這是第二個集合

x = itemsA.union(itemsB)
y = itemsA.intersection(itemsB)
ans=x-y
lst=list(ans)
lst.sort()
print(lst)
