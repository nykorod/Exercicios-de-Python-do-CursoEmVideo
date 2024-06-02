n=[]
r=' '
while r not in 'n':
       n.append(int(input('numero:  ')))
       r=' '
       while r not in 'sn':
              r=str(input('quer continuar? [s/n]:  ').strip().lower()[0])
n.sort(reverse=True)
print(f'''voce digitou {len(n)} numeros
os numeros digitados foram: {n}''')
if 5 in n:
       print(f'voce digitou o numero 5')
else:
       print(f'voce nao digitou o numero 5')