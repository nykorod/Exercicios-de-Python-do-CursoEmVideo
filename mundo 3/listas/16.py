# dados=[]
# dados.append('Pedro')
# dados.append('25')
# # print(dados)

# dados2=[]
# dados2.append('maria')
# dados2.append('34')
# pessoas.append(dados[:],dados[:])
# pessoas=[['pedro', 25], ['maria', 19],['joao', 32]]
# print(pessoas[1])
p=[]
n=[]
for c in range(0,3):
       n.append(input('nome: '))
       n.append(int(input('idade: ')))
       p.append(n[:])
       n.clear()
print(p)
