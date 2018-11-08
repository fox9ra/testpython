# put your python code here
n = int(input())
c = 1
s=[]
while c <= n:
    s += [c] * c
    c += 1
    if len(s) == n:
    	break

s=s[0:n]
for i in s:
	print(i,end=' ')