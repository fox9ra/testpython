s = input()
n = 0
k=len(s)
c=1
for i in s:
	if (k-1 <= n):
		print (s[n] + str(c), end='')
		break
	else:
		if (s[n] == s[n+1]):
			c+=1
		else:
			print (s[n], c, end='',sep='')
			c=1
	n += 1