alunos=[]
r=' '
c=n=0
while r not in 'n':
       nome=input('nome:  ')
       n1=float(input('nota 1:  '))
       n2=float(input('nota 2:  '))
       m=(n1+n2)/2
       alunos.append([nome,[n1,n2],m])
       r=input('continuar? [s/n]:  ').strip().lower()[0]
       while r not in 'sn':
              r=input('continuar? [s/n]:  ').strip().lower()[0]
       c+=1
print(f'{'no.':<4}{'nome:':<20}{'media:':>5}')
for a, i in enumerate(alunos):
       print(f'{a:<4}{i[0]:<20}{i[2]:>5.1f}')
while n != 999:
       n=int(input('mostrar notas de qual aluno? (999 para parar):  '))
       if n == 999:
              break
       if n>len(alunos)-1:
              print('numero invalido!')
       else:
              print(f'as notas desse aluno foram:  {alunos[n][1]}')
       print('-='*20)
