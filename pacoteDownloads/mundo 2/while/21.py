s=c=n=0
n=int(input('numero[999 para]:  '))
while n != 999:
       s+=n
       c+=1
       n=int(input('numero[999 para]:  '))

print('voce digitou {} numeros! a soma foi de {}'.format(c,s))