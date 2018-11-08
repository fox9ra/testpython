n="n5a12d5c1"
s=0
while s<len(n):
	if n[s].isalpha():
		bukva=n[s]
		cifra=""
	elif n[s].isdigit():
		cifra=cifra + n[s]
		if s+1==len(n):
			print(bukva*int(cifra), end='')
		elif n[s+1].isalpha():
			print(bukva*int(cifra), end='')
	s+=1