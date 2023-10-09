'''Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.'''
lista = list()
listaI = list()
listaP = list()
resp = str
while resp != 'N':
    lista.append(int(input('Digite um valor: ')))
    resp = input('Gostaria de digitar mais algum valor? [S/N]: ').strip().upper()[0]
for c in lista:
    if c%2 == 0:
        if c !=0:
            listaP.append(c)
    else:
        listaI.append(c)
print('-'*40)
print(f'Lista informada: {lista}')
print(f'Lista dos números pares informado: {listaP}')
print(f'Lista dos números ímpares informado: {listaI}')
