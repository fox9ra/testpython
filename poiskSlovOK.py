
all = open('dataset_3363_3 (1).txt', 'r')
s = all.read().lower().strip().split()
y = 0
m =''
for i in s:
    z = s.count(i)
    if z > y:
        y = z
        m = i
    elif z == y and i < m:
        m = i
print(m, y)