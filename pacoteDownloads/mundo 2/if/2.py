casa = float(input('quanto vai ser a casa?: '))
sal = float(input('quanto voce ganha?: '))
anos = float(input('quantos anos vai financiar?: '))
pm = casa/(anos*12)
min = sal*(30/100)
if pm <= min:
       print('pode financiar')
else: 
       print('nao pode')
       