from random import randint
from operator import itemgetter
from time import sleep
dado={'jogador1': randint(1,6),
      'jogador2': randint(1,6),
      'jogador3': randint(1,6),
      'jogador4': randint(1,6),}
rank=()
print('-='*10)
for k,v in dado.items():
  print(f'{k} tirou {v}')
  sleep(0.4)
print('-='*10)
rank= sorted(dado.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(rank):
  print(f'{i+1}°: {v[0]} com {v[1]}')
  sleep(0.4)
print('-='*10)

# dado={}
# jogo={}

# for c in range (0,4):
#   print(f'\no jogador {c} jogou', end=' ')
#   dado['numero']=randint(1,6)
#   print(dado['numero'])
#   jogo=['jogador'] (dado.copy())
# for k,v in enumerate(jogo):
#   print(k)
