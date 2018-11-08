def modify_list(l):
	k=len(l)-1
	while k >= 0:
		if l[k]%2 == 0:
			l[k]=int(lst[k]/2)
			print (k, l[k], "Четное")
		else:
			print (k, l[k], "НеЧетное")
			del l[k]
		k-=1
	
lst = [10,5,8,3]
modify_list(lst)
print (lst)
