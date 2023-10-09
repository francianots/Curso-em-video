while True:
    numerosE = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte') 
    n = int(input('Digite um núemro de 0 a 20: '))
    while True:
        if n < 0 or n > 20:
            print('Número digitado é invalido.')
            n = int(input('Digite um núemro de 0 a 20: '))
        else:
            print(f'Você digitou o número {numerosE[n]}.')
            r = input('Gostaria de digitar outro número? [S/N]: ').strip().upper()[0]
            break
    if r == 'N':
        break