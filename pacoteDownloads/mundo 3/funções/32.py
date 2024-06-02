# def msg(msg):
#      print('-'*30)
#      print(msg)
#      print('-'*30)
# msg('oi')

# def soma(a,b):
#      print(a+b)
# soma(5,6)

# def cont(*num):
#      print(num)
#      print(f'foram informados {len(num)} valores ao todo')
# # cont(43,4,6,7,5,3,3,2,3)

# def dobra(lista):
#      cont=0
#      while cont < len(lista):
#           lista[cont] *= 2
#           cont+=1
# n=[1,54,7,5,3,7,9,7,5,3,5]
# dobra(n)
# print(n)

def soma(*n):
     s=0
     for num in n:
          s+=num
     print(f'a soma entre {n} é {s}')
soma(1,3,54,6)
soma(5,8,6)