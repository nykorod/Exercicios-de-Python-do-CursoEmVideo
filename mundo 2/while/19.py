n=int(input('inicio da PA:  '))
r=int(input('razão da PA:  '))
# c vai ser o contador, quando ele for menor ou igual ao total, o loop vai funcionar
c=1
# total é o total de termos que o cliente vai querer, serve para controlar o loop da PA junto do c
total=0
# t é o numeros de termos, ele vai servir para poder add mais termos apos os 10 primeiros
t=10

# add mais termos, e acaba o loop quando a pessoa digitar 0
while t > 0:
       total+=t
       while c <= total:
              print(' {} ->'.format(n), end='')
              # coisa de PA
              n+=r
              # cada loop vai add 1 no contador, controlando o loop, ja que c n pode ser maior que o total
              c+=1
       print('pausa')
       t=int(input('voce gostaria de adicionar mais termos?:  '))


       
