'''Faça um programa que leia 5 valores númericos e guarde os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.'''
maiorN = menorN = 0
valores = list()
for c in range(0,5):
    valores.append(int(input(f'Digite um númeropara posição {c}: ')))
    if c == 0:
        maiorN = menorN = valores[c]
    else:
        if valores[c] > maiorN:
            maiorN = valores [c]
        elif valores[c] < menorN:
            menorN = valores[c] 
print('-'*45)
print(f'Os números digitados formal a seguinte lista: {valores}')
print(f'O maior número digitado foi o {maiorN}, nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maiorN:
        print(f'{i}... ', end='')
print(f'\nO menor número digitado foi o {menorN}, nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menorN:
        print(f'{i}... ', end='')