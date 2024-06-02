lista = ['aprender', 'python']
for palavra in lista:
       print(f'\nna palavra {palavra} temos ',end='')
       for letra in palavra:
              if letra.lower() in 'aeiou':
                     print(letra, end='')
       # r = ''.join([letra for letra in palavra if letra.lower() in 'aeiou'])
       # print(f'na palavra {palavra} temos {r}')
