def linha(tam = 42):
  return '-' * tam


def cab(txt): 
  print(linha())
  print(txt.center(42))
  print(linha())


def menu(lista):
  cab('menu principal')
  c = 1
  for item in lista:
    print(f'{c} - {item}')
    c += 1
  print(lista)