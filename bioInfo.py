#ex 3.7.2
#входные данные
a=input()
b=input()
slovo=input()
shifr=input()

#заполнение словаря функция zip
d=dict(zip(a,b))

print(*((d.get(i)) for i in slovo))
print (d)
#инверсия словаря
d = {v:k for k, v in d.items()}
print(*((d.get(i)) for i in shifr))

#print (a,b)
print (d)