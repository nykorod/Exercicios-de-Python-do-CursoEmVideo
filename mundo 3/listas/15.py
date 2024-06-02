t=str(input('digite uma expressao:  '))
for p in t:

       if t.count(')') > t.count('(') or p in ')' and t.count(')') ==0:
              print('expressao invalida')
              break
if t.count(')') == t.count('('):
       print('expressao valida')
else:
       print('expressao invalida')