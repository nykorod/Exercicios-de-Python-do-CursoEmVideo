def comando(no):
     help(no)

def titulo(msg):
     print('~'*int(len(msg)+2))
     print(f' {msg}')
     print('~'*int(len(msg)+2))

while True:
     titulo('SISTEMA DE AJUDA PyHELP')
     n=input('comando:  ')
     if n.lower() == 'fim':
          break
     else:
          comando(n)