lista=(int(input('digite um numero:  '))), (int(input('digite um numero:  '))), (int(input('digite um numero:  '))), (int(input('digite um numero:  '))), 
print(f'voce digitou {lista}')
print(f'o 9 apareceu {lista.count(9) } vez(es)')
if 3 in lista:
       print(f'o 3 aparece na posicao {lista.index(3)+1}')
else:
       print('nao tem numero 3')
print(f'os numeros pares foram: ', end='')
for n in lista:
       if n % 2==0:
              print(f'{n}', end='')

# lista=[]
# pares=[]
# count=0
# for c in range(1,5):
#        n=int(input('digite um numero:  '))
#        lista.append(n)
#        if n%2==0:
#               pares.append(n)
#        if n==9:
#               count+=1
# print(f'''voce digitou {lista} 
# o numero 9 apareceu {count} vez(es)''')
# if 3 in lista:
#        print(f'o 3 aparece na posicao {lista.index(3)+1}')
# else:
#        print('nao tem numero 3')
# print(f'os numeros pares digitados foram: {pares}')

                                                                                                                                                                                                                                                                                                                                    