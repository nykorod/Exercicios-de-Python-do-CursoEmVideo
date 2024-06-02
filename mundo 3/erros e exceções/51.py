# principais erros:
# NameError é quando uma variavel n existe

def leiaint(msg):
     while True:
          try:
               a=int(input(msg))
          except (ValueError, TypeError):
                    print('não é número')
                    continue
          except (KeyboardInterrupt):
               print()
               print(f'\033[0;31mO usuario preferiu não digitar\033[m')
               return 0
          else:
               return a

def leiafloat(msg):
     while True:
          try:
               a=float(input(msg))
          except (ValueError, TypeError):
                    print('não é número')
                    continue
          except (KeyboardInterrupt):
               print()
               print(f'\033[0;31mO usuario preferiu não digitar\033[m')
               return 0
          else:
               return a
                
# import a
a=leiaint('inteiro:  ')
b=leiafloat('decimal:  ')
print(f'o valor inteiro digitado foi: {a}, e o valor decimal foi: {b}')
# a=float(input('msg'))
# # c=a.leiaint('inteiro:  ')
# # b=a.leiafloat('decimal:  ')
# if a == '':
#      a=0
# print(a)
#  (f'o cliente não quis continuar')
