i18=m=m20=0
while True:
       sex=pause=' '
       print('-='*15)
       i=int(input('idade:  '))    
       while sex not in 'FM':
              sex=str(input('sexo [f/m]:  ').upper().strip()[0])
       while pause not in 'SN':
              pause=str(input('quer acabar? [s/n]:  ').upper().strip()[0])
       if i > 18:
              i18+=1
       if sex in 'Mm':
              m+=1
       if sex in 'Ff' and i < 20:
                     m20+=1
       if pause in 'Ss':
              break
print(f'''tem {i18} pessoas com mais de 18 anos
tem {m} pessoas masculinas
tem {m20} mulheres com menos de 20 anos''')
