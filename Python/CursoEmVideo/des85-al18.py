'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
num = [[], []]
for c in range (1,8):
    n = int(input(f'Digite o {c}° número: '))
    if n%2 == 0 and n != 0:
        num[0].append(n)
    elif n%2 != 0:
        num[1].append(n)
print('-'*40)
print(f'Valores informados: {num}')
print(f'Valores pares: {sorted(num[0])}')
print(f'Valores ímpares: {sorted(num[1])}')