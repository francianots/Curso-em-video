'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número ja exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
valores = list()
while True:
    n = int(input('Digite um número: '))
    if n in valores:
        print('O este número ja existe na lista. Favor informar um diferente. ')
    else:
        valores.append(n)
    resp = input('Gostaria de adicionar mais um número a lista? [S/N]: ').strip().upper()[0]
print(valores)        