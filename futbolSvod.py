#ex 3.7.1
#c=int(input("Кол игр:"))
c=int(input())
#c=int(input())
#создание пустого словаря игр
d={}

#функция поиска по ключу и прибавления очков
def keyfind(key,kv,kn,kp,ks):
	if key in d:
		print ('ключ1 есть')
		d[key][0]+=1
		d[key][1]+=kv
		d[key][2]+=kn
		d[key][3]+=kp
		d[key][4]+=ks
	else:
		print ('ключа нет')
		d[key]=[0]*5
		d[key][0]+=1
		d[key][1]+=kv
		d[key][2]+=kn
		d[key][3]+=kp
		d[key][4]+=ks


for i in range(c):
#ввод игр
	#k1, s1, k2, s2=input("Игра:").split(';')
	k1, s1, k2, s2=input().split(';')
	#print(k1, s1, k2, s2)
#присвоение очков
	if s1 > s2:
		ks1=3
		kv1=1
		kp1=0
		kn1=0
		ks2=0
		kv2=0
		kp2=1
		kn2=0
		keyfind(k1,kv1,kn1,kp1,ks1)
		keyfind(k2,kv2,kn2,kp2,ks2)
	elif s1==s2:
		ks1=1
		kv1=0
		kp1=0
		kn1=1
		ks2=1
		kv2=0
		kp2=0
		kn2=1
		keyfind(k1,kv1,kn1,kp1,ks1)
		keyfind(k2,kv2,kn2,kp2,ks2)
	else:
		ks1=0
		kv1=0
		kp1=1
		kn1=0
		ks2=3

for key in d:
	print (key,end=':')
	print (d[key][0],d[key][1],d[key][2],d[key][3],d[key][4])


'''
#Good from stepik
def command(c, res):
    if not c in dct: dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [dct[c][0] + 1, 
                dct[c][1] + 1 if res == 3 else dct[c][1],
                dct[c][2] + 1 if res == 1 else dct[c][2],
                dct[c][3] + 1 if res == 0 else dct[c][3],
                dct[c][4] + res,]  
dct = {}
for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')    
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))
'''
