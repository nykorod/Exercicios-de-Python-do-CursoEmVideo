aluno={}
aluno['nome']=input('nome:  ')
aluno['media']=float(input('media:  '))
print(f'aluno(a): {aluno["nome"]}')
print(f'media: {aluno["media"]}')
if aluno['media']>6:
  print('aprovado(a)')
else:
  print('reprovado(a)')