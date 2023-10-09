'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, ja na posição correta de inserção (sem usar sort()).
No final, mostre a lista ordenada na tela.'''
lista = list()
print('-'*40)
for c in range(5):
    n = int(input('Digite o elemento desejado: '))
    if c == 0 or n >= lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos +=1
    print('-'*40)
    print(lista)
print('-'*40)
