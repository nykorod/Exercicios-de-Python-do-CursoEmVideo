from random import randint
def sum2():
     n=[]
     par=[]
     s=0 
     for c in range(0,5):
          n.append(randint(1,10))
     print(f'os valores sorteados foram: ', end=' ')
     for num in n:
          print(f'{num}', end=' ')
          if num % 2 == 0:
               par.append(num)
               s+=num
          print(f'a soma dos valores {par} é {s}')
sum2()
