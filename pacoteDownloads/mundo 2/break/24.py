s=c=0
while True:
       n=int(input('digite um numero [999 = parar]:  '))
       if n==999:
              break
       s+=n
       c+=1
print(f'voce digitou {c} digitos e a soma deu {s}')
