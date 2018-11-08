with open('dataset_3363_2.txt') as inf, open("test2.txt", 'w') as ous:
    for n in inf:
        n = n.strip()
        s=0
        while s<len(n):
        	if n[s].isalpha():
        		bukva=n[s]
        		cifra=""
        	elif n[s].isdigit():
        		cifra=cifra + n[s]
        		if s+1==len(n):
        			ous.write(bukva*int(cifra))
        		elif n[s+1].isalpha():
        			ous.write(bukva*int(cifra))
        	s+=1
