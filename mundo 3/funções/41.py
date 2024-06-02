def ficha(nome='desconhecido', gol=0):
     print(f'O jogador {nome} ', end='')
     if gols < 1:
          print(f'fez nenhum gol no campeonato.')
     else:
          print(f'fez {gol} gols no campeonato')

nome=str(input('nome:  '))
gols=str(input('gols:  '))
if gols.isnumeric():
     gols=int(gols)
else:
     gols=0
if nome.strip() == '':
     ficha(gol=gols)
else:
     ficha(nome, gols)