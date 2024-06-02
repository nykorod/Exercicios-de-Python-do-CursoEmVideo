nome=[]
peso=[]
r=' '
while r not in 'n':
       n= input('nome:  ')
       p=int(input('peso:  '))
       peso.append(p)
       nome.append(n)
       r=' '
       while r not in 'sn':
              r=str(input('quer continuar? [s/n]:  ').strip().lower()[0])
print(f'voce cadastrou {len(nome)} pessoas')
print(f'o mais pesado(a) é {nome[peso.index(max(peso))][0]} com o peso de {max(peso)}')
