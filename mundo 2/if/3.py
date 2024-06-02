import random
from time import sleep
item = random.randint(0,2)

print('''vamos jogar jokenpo!
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogada= int(input('escolha:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
minha_lista = ['pedra', 'papel', 'tesoura']
print('voce escolheu {}, e o computador escolheu {}!'.format(minha_lista[jogada], minha_lista[item]))

if item == 0:
       if jogada == 0:
              print('empatou')
       elif jogada == 1:
              print('ganhou, ze buceta')
       else:
              print('perdeu! otario')
elif item == 1:
       if jogada == 0:
              print('perdeu! otario')
       elif jogada == 1:
              print('empatou')
       else:
              print('ganhou, ze buceta') 
elif item == 2:
       if jogada == 0:
              print('ganhou, ze buceta')
       elif jogada == 1:
              print('perdeu! otario')
       else:
              print('empatou')
