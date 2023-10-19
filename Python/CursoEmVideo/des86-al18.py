'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
for i, l in enumerate(matriz):
    for c in range(len(l)):
        matriz[i][c] = int(input(f'Digite o valor da {i+1}ª linha, {c+1}ª coluna: '))
for l in range(0, 3):
    print('-'*30)
    for c in range(0, 3):
        print(f'|{matriz[l][c]:^8}|',end='')
    print()
print('-'*30)