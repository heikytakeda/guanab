from .test import cab
from .test import menu
from .test import linha
from time import sleep

cab('SISTEMA DE ARQUIVOS')
while True:
  resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
  if resposta == 1:
    cab('opc 1')
  elif resposta == 2:
    cab('opc 2')
  elif resposta == 3:
    cab('Saindo do sistema...ate logo!')
    break
  else:
    print('\033[31mERRO! Digite uma opcao valida.\033[m')
  sleep(1)
