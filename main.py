from sistema import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
  CriarArquivo(arq)

cab('SISTEMA DE ARQUIVOS')
while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
  if resposta == 1:
    lerArquivo(arq)
  elif resposta == 2:
    cab('NOVO CADASTRO')
    nome = str(input('nome: '))
    idade = leiaint('idade: ')
    cadastrar(arq, nome, idade)
  elif resposta == 3:
    cab('Saindo do sistema...ate logo!')
    break
  else:
    print('\033[31mERRO! Digite uma opcao valida.\033[m')
  sleep(1)
