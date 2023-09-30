'''Faça um programa que leia um número de 0 a 9999
 e mostre na tela cada um dos digitos separados.

 Ex:
 Digite um número: 1834

 Unidade: 4
 Dezena: 3
 Centena: 8
 milhar: 1'''

print('-----------------------------------------------------------')
num = int(input('Digite um numero:'))
u = num // 1 % 10
c = num // 10 % 10
d = num // 100 % 10
m = num // 1000 % 10
print('-----------------------------------------------------------')
print('')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
