from time import sleep
def contador(a,b,c):
     if c == 0:
          c=1
     if c < 0:
          c*=-1
     if a<b:
          while a<=b:
               print(f'{a} ', end='',flush=True)
               sleep(0.5)
               a+=c
     else:
          while a>=b:
               print(f'{a} ', end='', flush=True)
               sleep(0.5)
               a-=c
     return a
contador(1,10,1)
print()
contador(20,0,2)
print()
contador(20,20,-8)
ini=int(input('inicio:  '))
fin=int(input('final:  '))
pas=int(input('passo:  '))
contador(ini, fin,pas)