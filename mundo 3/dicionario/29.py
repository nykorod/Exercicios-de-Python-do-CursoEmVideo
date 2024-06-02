resp=' '
pessoas=[]
pessoa={}
idades=[]
mulheres=[]
acimamedia=[]
nome=[]

while resp not in 'n':

     resp=' '
     pessoa['nome']=input('nome:  ')
     nome.append(pessoa['nome'])

     pessoa['idade']=int(input('idade:  '))
     idades.append(pessoa['idade'])

     pessoa['sexo']=input('sexo[f/m]:  ').strip().lower()[0]
     while pessoa['sexo'] not in 'fm':
          pessoa['sexo']=input('sexo[f/m]:  ').strip().lower()[0]
     if pessoa['sexo'] in'f':
          mulheres.append(pessoa['nome'])
     pessoas.append(pessoa.copy())

     while resp not in 'sn':
          resp=input('continuar?: [s/n]').strip().lower()[0]

media= sum(idades)/len(idades)
for idade in idades:
     if idade > media:
          acimamedia.append(nome[idades.index(idade)])

print(f'''A) {len(pessoas)} pessoas cadastradas
B) a media das idades foi  de {media} anos
C) as mulheres cadastradas foram {mulheres}
D) idade acima da media {acimamedia}''')


