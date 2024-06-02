
# ! Isso é um comentário crítico 
# ? Isso é uma questão ou um comentário de dúvida
# * Este é um comentário importante
# TODO: Implementar a função de login
# Este é um comentário normal

# tupla
n= (2,8,9,1)
# lista
n= [2,8,9,1]

n[2]=3
# add item a lista
n.append(6)

# botar em ordem numerica/alfabetica ou invertida
n.sort(reverse=True)

# add 0 ao na terceira posicao da lista
n.insert(3,0)
n.insert(2,1)

# remove o ultimo item da lista
# n.pop()

# remove o item na posicao desejada
n.pop(1)

# remove a primeria ocorrencia do item selecionado
n.remove(2)
print(n)
print(f'essa lista tem {len(n)} itens')
# da pra transformar tupla em lista, e lista é mutavel
n.sort()
for p, v in enumerate(n):
       print(f'{v} na posicao {p+1} ')
