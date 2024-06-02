import random
from time import sleep
lista=[]
jogos=[]
n=int(input('quantos jogos voce quer sortear?:  '))
while True:
       for c in range(0,5):
              sort=random.randint(1,60)
              if sort not in lista:
                     lista.append(sort)
       if n == 0:
              break
       lista.sort()
       jogos.append(lista[:])
       lista.clear()
       n-=1
for n, r in enumerate(jogos):
       print(f'jogo {n+1}: {r}')
       sleep(0.5)
       