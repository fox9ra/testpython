k=[]
used=[]
a=[int(i) for i in input().split()]
for i in a:
	c=a.count(i)
	if c>1:
		k.append(i)
unique = [used.append(x) for x in k if x not in used]
used.sort()
for i in used:
	print (i,'',end='')
