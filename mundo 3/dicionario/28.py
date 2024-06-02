jogador={}
gols=[]
jogador['nome']= input('nome:  ')
c=int(input(f'quantas partidas {jogador['nome']} fez?:  '))
for jogo in range(0,c):
     gols.append(int(input(f'quantos gols na partida {jogo+1}?:  ')))
jogador['gols']=gols.copy()
jogador['total']=sum(gols)
print(jogador)
for k,v in jogador.items():
     print(f'{k} = {v}')
for i, v in enumerate(gols):
     print(f'o jogador {jogador["nome"]} fez {v} gols no jogo {i+1}')