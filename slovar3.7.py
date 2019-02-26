#ex 3.7.3
#создаем пустой список
s=[]
k=[]
#по циклу пока не будет больше добавляем элемент в конец списка
for i in range(int(input())):
    s.append(input().lower())
    
#print (s)
#читаем вход строк для проверки
for c in range(int(input())):
    c=input().lower().strip().split()
    for i in c:
#проверяем если нет в списке то добавляем в другой список
        if i not in s:
            k.append(i)
#преобразуем в множество
c=set(k)
for i in c:
    print(i)

'''
#good from stepic
# формируем множество известных слов на основании построчного ввода
dic = {input().lower() for _ in range(int(input()))}

# заводим пустое множество для приема текста
wrd = set()

# т.к. текст построчно подается, а также в каждой строке несколько слов,
# то каждую строку превращаем во множество и добавляем в единое множество wrd
for _ in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

# на вывод отправляем результат вычитания словарного множества dic
# из текстового множества wrd; впереди ставим *, чтобы раскрыть поэлементно
print(*(wrd-dic), sep="\n")
'''


'''
#good from stepik2
# put your python code here
words = set(input().lower() for i in range(int(input())))
text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
print('\n'.join(text - words))
'''
