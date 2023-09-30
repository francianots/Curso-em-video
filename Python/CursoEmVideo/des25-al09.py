'''Crie um programa que leia o nome de uma pessoa
 e diga se ela tem "Silva" no nome'''
print('----------------------------------------------------')
nome = input('Digite seu nome completo:')
print('----------------------------------------------------')
print('')
nome = nome.title()
i = nome.find('Silva')
print(f'nome: {nome}')
print(f'Possui "Silva" no nome: {i>-1}')
print('----------------------------------------------------')
