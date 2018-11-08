# put your python code here
n = int(input())
c = 0
s=[]
while len(s) < n:
    s += [c] * c
    c += 1
print(*s[:n])