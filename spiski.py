n=-1
a=[int(i) for i in input().split()]
ma=len(a)-1
k=0
if ma == 0:
	print (a[0])
else:
	for i in a:
		n+=1
		if (n==0):
			k=a[1]+a[len(a)-1]
		elif (n==len(a)-1):
			k=a[len(a)-2]+a[0]
		else:
			k=a[n-1]+a[n+1]
		print (k,'',end='')