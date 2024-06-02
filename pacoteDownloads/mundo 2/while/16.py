print('ola! estou pensando em um numero entre 0 e 10!')
import random
item= random.randint(0,10)
s=0
acertou= False
while not acertou:
       n=int(input('qual seu palpite?:  '))
       if n>item:
              print('menos!')
       if n<item:
              print('mais!')
       s+=1
       if n == item:
              acertou=True
print('correto!')
print('voce precisou de {} tentativas!'.format(s))