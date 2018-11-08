def f(x):
	x=x*2
	return x

#c=int(input("Кол попыток:"))
c=int(input())
d={}
for i in range(c):
	#n=int(input("число:"))
	n=int(input())
	if n in d:
		#print ('ключ есть')
		print(d[n])
	else:
		#print ('ключа нет')
		d[n]=f(n)
		print(d[n])
#print (d)