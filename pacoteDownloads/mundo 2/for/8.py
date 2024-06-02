s=0
co=0
for c in range(1,7):
       n= int(input('numero: '))
       if n % 2 == 0:
              co+=1
              s+=n
print('tem {} pares e a soma é {}'.format(co,s))
