c=1
p=i=0
while c !=0:
       c= int(input('numero: '))
       if c!= 0:
              if c % 2 == 0:
                     p+=1
              else:
                     i+=1
print('tem {} pares e {} impares'.format(p, i))
print('cabo')

# for é bom para repetição que sabe p fim e while para repetição com fim desconhecido