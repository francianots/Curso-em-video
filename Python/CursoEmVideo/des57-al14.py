'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado peça a digitação novamente até ter um valor correto.'''
print('----------------------------------------------------------------------')
print('                 V A L I D A D O R  D E  S E X O')
print('----------------------------------------------------------------------')
print('')
sexo = input('Digite seu sexo: [M/F]: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados invalidos. Digite seu sexo: [M/F]: ').strip().upper()[0]
    print('----------------------------------------------------------------------')