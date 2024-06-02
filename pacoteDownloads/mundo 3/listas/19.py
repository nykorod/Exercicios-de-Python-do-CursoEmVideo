lista=[[],[]]
valor=0
for c in range(0,7):
       valor=(int(input('numero:  ')))
       if valor %2==0:
              lista[0].append(valor)
       else:
              lista[1].append(valor)   
lista[0].sort()
lista[1].sort()
print(f'os numeros pares foram : {lista[0]}', end='')
print(f'\nos numeros impares foram : {lista[1]}', end='')

# lista=[]
# for c in range(0,7):
#        lista.append(int(input('numero:  ')))
# print(f'os numeros pares foram :', end='')
# lista.sort()
# for n in lista:
#        if n % 2 ==0:
#               print(n, end=' ')
# print(f'\nos numeros impares foram :', end='')
# for n in lista:
#        if n % 2 ==1:
#               print(n, end=' ')

              