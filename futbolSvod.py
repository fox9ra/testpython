def f(x):
	
	return x

c=int(input("Кол игр:"))
#c=int(input())
d={}

for i in range(c):
	k1, s1, k2, s2=input("Игра:").split(';')
	print(k1, s1, k2, s2)
	if s1 > s2:
		ks1=3
		ks2=0
	elif s1==s2:
		ks1=1
		ks2=1
	else:
		ks1=0
		ks2=3
	print(ks1, ks2)
	if k1 in d:
		print ('ключ1 есть')
		d[k1][0]+=1
	else:
		#print ('ключа нет')
		d[k1]=[0]*4
		print(d[k1])
print (d)


'''
a=[0]*5
b=[1]*5
d={'a':a, 'b':b}
print(d)
d['a'][0]=1
d['b'][1]=5
print(d)
'''