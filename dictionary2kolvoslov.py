a = [str(i) for i in input().split()]
print (a)
d={}
for i in a:
	i=i.lower()
	if i in d:
		#print ('ключ есть')
		d[i]+=1
	else:
		#print ('ключа нет')
		d[i]=1

for key, value in d.items():
    print(key, value)