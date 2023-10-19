'''Faça um programa que leia nome e média de um aluno, guardando tambem a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela'''
lista = {}
lista['nome'] = input('Nome: ')
lista['media'] = float(input('Media: '))
if lista['media'] >= 7:
    lista['situação'] = 'Aprovado'
elif lista['media'] >= 5 :
    lista['situação'] = 'Recuperação'
else: 
    lista['situação'] = 'Reprovado'
for k, v in lista.items():
    print(f'{k} é igual a {v}')
