n1=int(input('digite um numero '))
n2=int(input('digite outro numero '))
s =n1+n2
m = n1*n2
d= n1/n2
#  "end = ' '" para nao quebrar a linha, "{:.3f}" para pegar 3 casas decimais
print('a soma é igual a {}, multiplicacao é {}'.format(s, m), end = ' ')
print('e a divisao é {:.3f}'.format(d))
