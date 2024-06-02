def notas(*n, res=False):
     '''
     -> analisa notas e situações de vários alunos.
     :param n: uma ou mais notas dos alunos (aceita vários parâmetros)
     :param res: (opcional) indica se deve ou não retornar a situação do aluno
     :return: dicionário com várias informações sobre a situação da turma'''
     a={}
     a['total']=len(n)
     a['maior']=max(n)
     a['menor']=min(n)
     a['media']=sum(n)/len(n)
     if res:
          if a['media'] < 4:
               a['situação']='reprovado'
          elif a['media'] < 7:
               a['situação']='recuperação'
          else:
               a['situação']='aprovado'
     return a

resp = notas(5,10, res=True)
print(resp)
help(notas)