'''desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for Impar. Desconsidere-o'''
print('----------------------------------------------------------------------')
print('                          S O M A  P A R')
print('----------------------------------------------------------------------')
print('')
s = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma de todos os números par digitado é {s}.')
print('----------------------------------------------------------------------')