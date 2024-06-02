lista='lapis', 1, 'borracha', 2,'caderno',15,'estojo',125
# n=0
print('-='*20)
print(f'{'MERCADÃO':^40}')
print('-='*20)
for c in range(0,len(lista)):
       if c % 2 == 0:
              print(f'{lista[c]:.<30}',end='')
       else:
              print(f'R$ {lista[c]:>6.2f}')

#        print(f'{listagem[n]:8} {'-'*20:20} R$ {float(listagem[n+1])}')
#        n+=2