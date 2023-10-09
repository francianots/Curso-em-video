while True:
    numeros = (int(input('Digite um número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o ultimo número: ')))
    print(f'O número 9 apareceu {numeros.count(9)} vezes.')
    if 3 in numeros:
        print(f'O número 3 foi digitado na  {numeros.index(3)}ª posição') 
    else:
        print('Não foi digitado o número 3.')
    print('Os números pares digitados foram : ', end='')
    for c in numeros:
        if c%2 == 0:
            print(f'{c}',end='  ')
    r = input('Gostaria de repetir? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break