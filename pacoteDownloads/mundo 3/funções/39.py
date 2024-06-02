def voto(n):
     from datetime import datetime 
     ano=datetime.now().year
     nsc=ano-n
     print(nsc)
     if nsc >= 18 and nsc <= 65:
          return f'voto obrigatorio'
     if nsc < 16:
          return f'voto negado'
     if nsc>=16 and nsc < 18 or nsc > 65:
          return f'voto opcional'


print(voto(2020))

