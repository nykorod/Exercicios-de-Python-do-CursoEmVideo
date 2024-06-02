dados={'nome': 'pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo']='m'
del dados['sexo']
dados['peso']='78'
print(dados)
print(dados.values())
print(dados.keys())
# for k,v in dados.items():
#   print(f'.;{k} é {v}')
print(f'o {dados["nome"]} tem {dados["idade"]} anos')
# para copiar o conteudo com o dicionario é diferente do a lista com [:], se usa .copy()