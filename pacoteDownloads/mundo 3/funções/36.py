a = []
def maior(*n):
     if len(n) == 0:
          return print('valor não encontrado')
     print(f'os valores dados foram: ',end='')
     for num in n:
          print(num, end=' ')
     print(f'\ne o maior valor encontrado foi: {max(n)}')


maior(2,5,8,3)
maior(7)
maior()