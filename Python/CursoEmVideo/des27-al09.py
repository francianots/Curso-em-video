'''Faça um programa que laia o nome complato de uma
pessoa, mostrando em seguida o primeiro a o último nome saparadamenta.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''
print('----------------------------------------------------------------------')
nome = input('Digite seu nome completo: ').split()
print('----------------------------------------------------------------------')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')
print(f'Seja bem vindo {nome[0]} {nome[len(nome)-1]}')
print('----------------------------------------------------------------------')

