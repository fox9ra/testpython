a = [int(i) for i in input().split()]
b = int(input())
c=1
if b in a:
	for x in a:
		if b == x:
			print (c-1, end=' ')
		c+=1
else:
	print ("Отсутствует")