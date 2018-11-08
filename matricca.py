a=[]
while True:
	n = input()
	if n == "end":
#		print ("end")
		break
	else:
		a.append([int(j) for j in n.split()])
#print ("OK",a)

z=-1
for i in a:
	z+=1
	x=-1
	for c in i:
		x+=1
#		print ("new=", c, z, x)

z+=1
x+=1
b = [[0] * x for i in range(z)]
for i in range(z):
	for j in range(x):
		b[i][j]=a[i-1][j]+a[i-len(a)+1][j]+a[i][j-1]+a[i][j-len(a[i])+1]
		print (b[i][j], end=' ')
	print ()