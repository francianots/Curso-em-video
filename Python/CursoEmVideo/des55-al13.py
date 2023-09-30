'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lido.'''
print('----------------------------------------------------------------------')
print('     I D E N T I F I C A D O R  M A I O R  E  M E N O R  P E S O')
print('----------------------------------------------------------------------')
print('')
maiorp = 0
menorp = 100000000
for c in range (1,6):
    p = float(input(f'Digite o peso da {c}ª pessoa [Kg]: '))
    if p > maiorp:
        maiorp = p
    if p < menorp:
        menorp = p
print('')
print('----------------------------------------------------------------------')
print(f'Maior peso registrado: {maiorp}Kg')
print(f'Menor peso registrado: {menorp}Kg')
print('----------------------------------------------------------------------')
