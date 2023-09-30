'''Faça um programa que calcule a soma entre todos os números ímpares
 que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
print('----------------------------------------------------------------------')
print('       M O S T R A D O R   DE   M Ú L T I P L O S  DE  T R Ê S')
print('----------------------------------------------------------------------')
s = 0
cs = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s += c
        cs += 1
print(f'A soma de todos os {cs} números múltiplos de três é {s}.')
print('----------------------------------------------------------------------')