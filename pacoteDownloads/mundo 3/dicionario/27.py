from datetime import datetime
anoatual=datetime.now().year
for c in range(0,1):
  pessoas={}
  pessoas['nome']=input('nome:  ')
  pessoas['idade']=anoatual-int(input('nascimento:  '))
  pessoas['carteira']=int(input('carteira de trabalho (0 = n tem):  '))
  if pessoas['carteira'] != 0:
    # pessoas['carteira']='não tem'
    # for k,v in pessoas.items():
    #   print(f'{k} = {v}')
    # break

    while len(str(pessoas['carteira'])) != 6:
      print('carteira invalida')
      pessoas['carteira']=int(input('carteira de trabalho (0 = n tem):  '))

    pessoas['sexo']=str(input('sexo [f/m]:  ')).lower().strip()[0]
    while pessoas['sexo'] not in 'fm':
      pessoas['sexo']=str(input('sexo [f/m]:  ')).lower().strip()[0]
      
    pessoas['contratação']=int(input('ano de contratação:  '))
    pessoas['salario']=float(input('salario:  '))
    if pessoas['sexo'] in 'm':
      pessoas['aponsentadoria']=35-(anoatual-pessoas['contratação']) + pessoas['idade']
    else:
      pessoas['aponsentadoria']=30-(anoatual-pessoas['contratação']) + pessoas['idade']
  else:
    pessoas['carteira']='não tem'
  for k,v in pessoas.items():
    print(f'{k} = {v}')
