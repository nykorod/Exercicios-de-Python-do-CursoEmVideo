estado={}
brasil=[]
for c in range(0,2):
  estado['uf']=input('uf:  ')
  estado['sigla']=input('sigla:  ')
  brasil.append(estado.copy())
for e in brasil:
  for k, v in e.items():
    print(f'{k} é {v}')