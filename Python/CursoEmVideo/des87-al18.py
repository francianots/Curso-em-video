'''Aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados.

b) A soma dos valores da terceira coluna.

c) O maior valor da segunda linha.'''


somaP = somaTC = maiorSL = 0
matriz = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para a {l+1}ª linha, {c+1}ª coluna: ')))
for l in range(0, 3):
    print('-'*30)
    for c in range(0, 3):
        print(f'|{matriz[l][c]:^8}|',end='')
        if matriz[l][c]%2 == 0:
            somaP += matriz[l][c] 
        if c == 2:
            somaTC += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorSL:
                maiorSL = matriz[l][c]
    print()
print('-'*30)
print('-='*35)
print(f'a)R: Soma de todos os valores pares: {somaP} ')
print(f'b)R: Soma de todos os valores da terceira coluna: {somaTC}')
print(f'c)R: Maior valor da segunda linha: {maiorSL}')