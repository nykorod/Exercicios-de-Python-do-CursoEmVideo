def leiaint(msg):
     while True:
          n=str(input(msg))
          if n.isnumeric():
               n=int(n)
               break
          else:
               print('\033[0;31mERRO! digite um numero inteiro valido.\033[m')
     return n

n=leiaint('numero: ')
print(f'voce digitou o numero {n}')