from random import randint
lista=[]
for c in range(1,6):
       n=randint(1,10)
       lista.append(n)
       print(n, end=' ')
print(f'\no maior foi o {max(lista)} e o menor foi {min(lista)}')
