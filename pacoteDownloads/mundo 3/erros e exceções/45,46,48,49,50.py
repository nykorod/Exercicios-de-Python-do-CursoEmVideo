# oq é modulo?
# surgiu na decada de 60
# ele reparte um programa gigante em varios programas menores
# fazendo com que o programa tenha:
# legibilidade e manuntenção faceis
# (imagina tentar achar uma linha de codigo que deu erro dentre 3000 linhas)


from . import a

# num=int((input('numero:  ')))
# fat=a.fac(num)
# print(f'o fatorial de {num} é {fat}')

p=a.ledin('valor:  ')

# print(f'{a.metade(p,False)}')
# print(f'{a.dobro(p)}')
# print(f'{a.aumentar(p,10)}')
# print(f'{a.diminuir(p,10)}')

a.resumo(p,80,35)