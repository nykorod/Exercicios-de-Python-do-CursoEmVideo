def inte(msg):
     return int(input(msg))
def metade(a,b=True):
     a=a/2
     return(m(a)) if b is True else a
def dobro(a,b=True):
     a=a*2
     return(m(a)) if b is True else a
def aumentar(a,b,c=True):
     a=a+(a*(b/100))
     return(m(a)) if c is True else a
def diminuir(a,b,c=True):
     a=a-(a*(b/100))
     return(m(a)) if c is True else a
def m(moeda):
    return f'R${moeda:.2f}'.replace('.', ',')
def ledin(msg):
    while True:
          a = input(msg).replace(',', '.')
          try:
               a = float(a)
               return a
          except ValueError:
               print(f'\033[0;31mERRO! "{a.strip()}" não é um número! Digite um número válido.\033[m')
def resumo(a, b, c): 
    print(f'{m(a)}')
    print(f'{dobro(a)}')
    print(f'{metade(a)}')
    print(f'Aumento de {b}% é {aumentar(a, b)}')
    print(f'Diminuição de {c}% é {diminuir(a, c)}')