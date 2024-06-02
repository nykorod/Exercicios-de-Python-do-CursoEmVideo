n=[]
while True:
       r=' '
       n.append(int(input('número:  ')))
# verificar se o n add ja existia
       if n.count(n[-1]) > 1:
              print('valor duplicado, não vou adicionar')
              n.remove(n[-1])
# remover n se existir
       while r not in 'sn':
              r=str(input('quer continuar? [s/n]:  ').strip().lower()[0])
       if r == 'n':
              break
n.sort()
print(f'os itens add foram: {n}')