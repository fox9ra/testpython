#ex 3.7.5
#создаем словаль со значениями в виде списка
d={ i:[] for i in range(1,12) }

#print (d)

#открываем файл
with open('dataset_3380_5.txt', 'r') as inf:
#идем по файлу
    for line in inf:
#сплитим файл
    	line = line.strip().split()
    	a, b, c = int(line[0]), line[1], int(line[2])
    	#print (a,"=",b,"=",c)
    	if a in d:
    		d[a].append(c)
    	#print (d)

for a in d:
	k=len(d[a])
	s=sum(d[a])
	if k==0:
		print(a,"-")
	else:
		c=s / k
		print (a,s / k)