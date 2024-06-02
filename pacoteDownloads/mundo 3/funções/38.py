# def soma(a=0,b=0,c=0):
#      s=a+b+c
#      print(s)
# soma(1)
# def teste():
#      n=1
#      print(n,x)

# x=2
# teste()
# * n tem escopo local por estar dentro de uma função e x tem escopo global por estar no programa principal
# * mesmo x estando na frente de n, a variavel ainda funciona na função

# def f():
#      n1=4
#      print(n1)
# n1=2
# f()
# print(n1)
# * se tiver 2 variaveis com o mesmo nome, a da função vai dominar dentro da função e a global vai dominar fora da função

def f(n2):
     global n1
     n1=8
     n2+=7
     print(n1)
     print(n2)
n1=2
print(n1)
f(n1)