'''Crie um programa que leia o nome completo de uma pessoa e mostre:

-O nome com todas as letras maiúsculas.
-O nome com todas as letras minúsculas.
-Quantas letras ao todo (sem considera espaços).
-Quantas letras tem o primeiro nome.'''
print('-----------------------------------------------------')
nome = str(input('Digite seu nome completo: ')).strip()
print('-----------------------------------------------------')
print('')
print(f'Seu nome em letras MAIÚCULAS: {nome.upper()}')
print(f'Seu nome em letras MINÚSCULAS: {nome.lower()}')
frase = nome.split(nome)
print(f'Quantas letras possui o seu nome completo: {len(nome) - nome.count(" ")}')
print(f'Quantas letras possui o seu primeiro nome: {nome.find(" ")}')
print('')
print('-----------------------------------------------------')
