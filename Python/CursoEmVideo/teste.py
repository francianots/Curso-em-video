'''07 – Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses
foram abertos e fechados na ordem correta. Exemplo:

(()) OK

()()(()()) OK

()) ERRO

Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhara-la a cada fecha
parênteses. Ao desempilhar, verifique se o topo da pilha é um abre parênteses. Se a expressão estiver
correta, sua pilha estará vazia no final.'''
r = str
while r != 'N':
  print('-'*45)
  exp = list(input('Digite uma sequência de parenses: '))
  print('-'*45)
  vExp = list()
  if exp[0] == '(' and exp[-1] == ')' and exp.count('(') == exp.count(')'):
    for c in exp:
      if c == '(':
        vExp.append(c)
      elif c == ')':
        vExp.pop()
    if len(vExp) == 0:
      print('A expressão foi digitada CORRETAMENTE.')
    else:
      print('A expressão foi digitada INCORRETAMENTE.')
  else:
    print('A expressão foi digitada INCORRETAMENTE.')
  print('-'*45)  
  r = input('Gostaria de tentar novamente? [S/N]:').strip().upper()[0]



