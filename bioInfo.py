#ex 3.7.2
#входные данные
a=input()
b=input()
slovo=input()
shifr=input()

#заполнение словаря функция zip
d=dict(zip(a,b))

#перебор элментов из slovo, поиск в d и сохранение в список 
st=[d.get(i) for i in slovo]
#вывод списка
print (''.join(st))
#инверсия словаря
d = {v:k for k, v in d.items()}
st=[d.get(i) for i in shifr]

#print (a,b)
print (''.join(st))

'''
#good from stepik
a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))
'''
