n= int(input('numero: '))
count=0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end= '')
        count += 1
    else:
        print('\033[31m', end= '')
    print('{} '.format(c), end= '')
if count > 2:
    print('\n\033[mO número {} não é primo.'.format(n))
else:
    print('O número {} é primo.'.format(n))
