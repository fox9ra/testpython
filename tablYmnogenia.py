a = int(input())
b = int(input())
c = int(input())
d = int(input())

for k in range(c,d+1):
    print ('\t', k, '\t', end='')
print()

for i in range(a,b+1):
	print (i, '\t', end='')
	for e in range(c,d+1):
		print (i*e, '\t', end='')
	print ()