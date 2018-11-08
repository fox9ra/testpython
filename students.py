s=0
m=0
st=[]
sumMat=0
sumFiz=0
sumRus=0
with open('dataset_3363_4.txt', "r" ,encoding='utf-8') as filein:
	for n in filein:
		st.append(n.strip().split(';'))
		s+=1
	#print(s)
	for x in st:
		mat=int(x[1])
		fiz=int(x[2])
		rus=int(x[3])
		sred=(mat+fiz+rus)/3
		print(sred)
		sumMat+=int(x[1])/s
		sumFiz+=int(x[2])/s
		sumRus+=int(x[3])/s
	print(sumMat, sumFiz, sumRus)
			
		
