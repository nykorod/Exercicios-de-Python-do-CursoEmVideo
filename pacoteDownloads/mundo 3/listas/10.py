n=[]
for c in range(0,5):
       n.append(int(input(f'digite um numero para posicao {c}:  ')))
print(f'o maior valor foi {max(n)} na posicao', end='')
for p,valor in enumerate(n):
       if valor==max(n):
              print(f' {p}...', end='')
print(f'\no menor valor foi {min(n)} na posicao', end='')
for p,valor in enumerate(n):
       if valor==min(n):
              print(f' {p}...', end='')
