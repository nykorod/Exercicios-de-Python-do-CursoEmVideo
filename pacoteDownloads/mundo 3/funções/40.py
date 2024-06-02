def fator(n, calc=False):
     ''''''
     f=1
     for c in range (n, 0, -1):
          if calc:
               print(f'{c}', end='')
               if c > 1:
                    print(f' x ', end='')
               else:
                    print(f' = ', end='')
          f*=c
     print(f)

fator(5)