'''Faça um programa que leia nome epeso de várias pessoas, guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.

b) Uma listagem com as pessoas mais pesadas.

c) Uma listagem com as pessoas mais leves.'''
ma = me = 0
resp = str
cadastro = []
temp = []
pesado = []
leve = []
while resp != 'N':
    temp.append(input('Nome: '))
    temp.append(input('Peso [Kg]: '))
    cadastro.append(temp[:])
    temp.clear()
    resp = input('Gostaria de adicionar mais uma pessoa? [S/N]: ').upper()[0]
for c in cadastro:
    if ma ==  0 and me == 0:
        ma = c[1]
        me = c[1]
    elif c[1] > ma:
        ma =  c[1]
        pesado = c[:]
    elif c[1] < me:
        me = c[1]
        leve = c[:]
print(cadastro[0][1])
print('-'*45)
print(f'Quantidade de pessoas cadastradas: {len(cadastro)}')
print(f'A pessoa mais pesada é {pesado[0]} com {pesado[1]}Kg.')
print(f'A pessoa mais leve é {leve[0]} com {leve[1]}Kg.')