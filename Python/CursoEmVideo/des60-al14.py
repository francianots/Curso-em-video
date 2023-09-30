'''Faca um programa que leia um número qualquer e mostre o seu fatorial.
ex:
5! = 5x4x3x2x1=120'''
print('--------------------------------------------------------------------')
print('           C A L C U L A D O R A  DE  F A T O R I A L')
print('--------------------------------------------------------------------')
n = int(input('Digite um número: '[1]))
f = 1
print (f'O fatorial de {n} é: ', end='')
for c in range (n,0,-1):
    print(c, end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
print(f)
print('--------------------------------------------------------------------')
