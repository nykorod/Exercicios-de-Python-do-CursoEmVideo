r='s'
c=s=0
lista=[]
while r in 'Ss':
       n=int(input('digite um valor:  '))
       r=str(input('quer continuar? [s/n]:  ').strip().upper()[0]) 
       s+=n
       c+=1
       lista.append(n)
m=s/c
print(f'voce digitou {c} numeros e a media é {m}')
print(f'o maior é {max(lista)} e menor {min(lista)}')