'''Crie um programa onde o úsuario digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem certa.'''
expre = input('Digite uma expressão para ser validada: ')
lista = list()
for c in expre:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
if len(lista) == 0:
    print('Sua espressão é valida!')
else:
    print('Sua espressão esta incorreta!')
print(expre)