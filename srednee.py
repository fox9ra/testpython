a = int(input())
b = int(input())
k = 0
c = 0
for i in range(a,b+1):
	if (i%3==0):
		k += 1
		c += i
print (c/k)