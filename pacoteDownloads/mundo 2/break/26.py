from random import randint
c=0
e=' '
while True:
       n=int(input('vamos jogar par ou impar! escolha um numero:  '))
       while e not in 'IP':
                     e=str(input('[I/P]:  ').strip().upper()[0])
       item=randint(1,11)
       res=n+item
       print(n+item)
       if e in 'Ii':
              if res % 2 == 1:
                     print('voce ganhou! parabens')
                     c+=1
              else:
                     print('voce perdeu!')
                     break
       if e in 'Pp':
              if res % 2 == 0:
                     print('voce ganhou! parabens')
                     c+=1
              else:
                     print('voce perdeu!')
                     break
       print(f'sequencia de {c} vitorias')
       