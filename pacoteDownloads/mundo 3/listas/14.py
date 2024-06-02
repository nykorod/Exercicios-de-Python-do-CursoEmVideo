n=[]
par=[]
impar=[]
r=' '
while r not in 'n':
       num=int(input('numero:  '))
       n.append(num)
       r=' '
       while r not in 'sn':
              r=str(input('quer continuar? [s/n]:  ').strip().lower()[0])
       if num %2==0:
              par.append(num)
       else:
              impar.append(num)
print(f'''voce digitou {n}
voce digitou {par} pares
e voce digitou {impar} impares''')
