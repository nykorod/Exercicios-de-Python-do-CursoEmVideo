n=int(input('digite um numero entre 0 e 20:  '))
e='zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
       if n >=0 and n<=20:
              print(f'voce pediu o numero {e[n]}')
              break
       else:
              n=int(input('errado! digite um numero entre 0 e 20:  '))
