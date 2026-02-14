from guanab.test import cab


def arquivoExiste(nome):
  try:
      a = open(nome, 'rt')
      a.close()
  except FileNotFoundError:
      return False
  else:
      return True
        

def CriarArquivo(nome):
  try:
      a = open(nome, 'wt+')
      a.close()
  except:
      print('Houve um problema na criacao do arquivo!')
  else:
       print(f'arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
  try:
       a = open(nome, 'rt')
  except:
       print('Erro ao ler arquivo!')
  else: 
      cab('PESSOAS CADASTRADAS')
      print(a.read())