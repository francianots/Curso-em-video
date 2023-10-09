'''Crie um programa que vai ler vários  números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''
resp = (str)
lista = list()
print('-'*40)
while resp != 'N':
    lista.append(int(input('Digite um valor: ')))
    print('-'*40)
    resp = input('Gostaria de adicionar mais um número ? [S/N]: ').strip().upper()[0]
    print('-'*40)
lista.sort(reverse= True)
print(f'lista em ordem decrescente: {sorted(lista)}')
print(f'Quantidade de elementos na lista: {len(lista)}')
print(f'Quantidade de números 5 na lista: {lista.count(5)}')