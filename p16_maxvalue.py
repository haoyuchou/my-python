score = 0
total = 0
ct = -1
maxvalue = 0
maxpo = 0

while score != -1:
    total += score
    ct += 1
    if score>maxvalue:
        maxvalue = score
        maxpo = ct
    score =eval(input())

print(total)
print(total/ct)
print(maxvalue)
print(maxpo)
