#ex3.7.4
d = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}

#функция поиска ключа
def keyfind(key,val):
	if key in d:
#		print ('ключ1 есть')
		d[key]+=val

#определение входных параметров
for i in range(int(input())):
    c=input().split()
    k=c[0]
#преобразование значения в int
    s=int(c[1])
    keyfind(k,s)
#    print (k,s)
#    print (d,c)
print(d['восток'] - d['запад'],d['север'] -d['юг'], end=' ')

'''
#good stepik
n=int(input())
d={'север':0,'запад':0,'юг':0,'восток':0}
for i in range(n):
    x=input().split()
    d[x[0]]+=int(x[1])
print(d['восток']-d['запад'], d['север']-d['юг'])
'''
