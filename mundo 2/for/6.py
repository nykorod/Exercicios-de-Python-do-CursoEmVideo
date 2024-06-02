s=0
count=0 
for c in range(1, 500, 2):
    if c % 3 == 0:
        # count vai contar quantas vezes esse if acontece e o s vai somar todos os if
        count+=1
        s += c
print('aqui esta o resultado da soma entre {}: {}'.format(count, s))
