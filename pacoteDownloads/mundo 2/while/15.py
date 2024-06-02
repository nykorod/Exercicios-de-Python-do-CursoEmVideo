s= str(input('qual o seu sexo?: ')).strip().upper()[0]
while s not in 'MmFf':
       s= str(input('invalido, qual o seu sexo?: ')).strip().upper()[0]
print('cadastrado!')
