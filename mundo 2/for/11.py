p = input('Palíndromo: ')
# Converte para minúsculas e remove espaços em branco
p = p.lower().replace(' ', '')
print(p[::-1])  
if p == p[::-1]:
    print('É palíndromo!')
else:
    print('Não é palíndromo.')
