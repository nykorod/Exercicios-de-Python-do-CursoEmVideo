k=0
m20=0
mv=[]
for c in range(1,5):
       print('pessoa {}'.format(c))
       n= input('nome: ')
       i= int(input('idade: '))
       s= input ('sexo: ')
       k+= i
       m= k/2
       mv.append(i)
       if c == 1 and s in 'Mm':
              mi=i  
              nv=n
       if s in 'Mm' and i > mi:
              # mi=i
              nv=n
       if s=='f':
              if i <= 20:
                     m20+= 1
print('media de idade é: {}'.format(m))
print('mulheres com menos de 20 anos: {}'.format(m20))
print('homem com maior idade é {}, com {} anos'.format(nv, mi))
