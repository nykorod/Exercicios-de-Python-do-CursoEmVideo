resp=' '
jogador={}
jogadores=[]
gols=[]
while resp not in 'Nn':
     jogador['nome']=input('nome:  ')

     partidas=int(input(f'quantas partidas {jogador['nome']} jogou?:  '))

     gols.clear()
     for partida in range(0,partidas):
          gols.append(int(input(f'quantos gols na partida {partida+1}?:  ')))
     jogador['gols']=gols[:]
     jogador['total']=sum(gols)
     jogadores.append(jogador.copy())

     resp=input('quer continuar? [s/n]:  ').strip()[0]
     while resp not in 'SsNn':
          resp=input('quer continuar? [s/n]:  ').strip()[0]

print('-='*25)
print(' cod', end=' ')
for k in jogador.keys():
     print(f'{k:<15}',end=' ')
print(f'')
print('-'*42)

for i,pessoa in enumerate(jogadores):
     print(f'{i:>4}', end=' ')
     for d in pessoa.values():
          print(f'{str(d):<15}',end
                =' ')
     print()

while True:
     n=int(input('qual jogador mostrar? [999 para parar]:  '))
     if n == 999:
          print('finalizando...')
          break

     if n > len(jogadores)-1:
          print('numero invalido!')

     else:
          print(f'dados do jogador {jogadores[n]['nome']}:')
          for i, gols in enumerate(jogadores[n]['gols']):
               print(f'  na partida {i+1} fez {gols} gols.')

     print('-'*42)
print('volte sempre')