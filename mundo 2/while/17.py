from time import sleep
n=int(input('ola! digite o primeiro numero:  '))
n2=int(input('ola! digite o segundo numero:  '))
r=0
while r != 5:
       sleep(0.5)
       print('-=-=-=-=-=-=-=-=-=-=-=-')
       print('''[ 1 ] somar
[ 2 ] multiplicar 
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair''')
       r=int(input('tudo certo! o que voce vai querer?:  '))
       if r==1:
              print(n+n2)
       if r==2:
              print(n*n2)
       if r==3:
              if n>n2:
                     print(n)
              else:
                     print(n2)
       if r==4:
              n=int(input('ola! digite o primeiro numero:  '))
              n2=int(input('ola! digite o segundo numero:  '))

sleep(0.5)
print('o programa esta desligando...')
sleep(1)
print('desligado')
sleep(0.5)