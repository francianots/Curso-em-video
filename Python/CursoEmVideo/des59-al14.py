'''Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
print('----------------------------------------------------------------------')
print('                  L E I T O R  DE  V A L O R E S')
print('----------------------------------------------------------------------')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('----------------------------------------------------------------------')
print('')
opc = 0
while opc != 5:
    print('''            ======================================
                            M E N U
            --------------------------------------
            [1]somar
            [2]multiplicar
            [3]maior
            [4]novos números
            [5]sair do programa
            ======================================''')
    opc = int(input('            >>>>>>>> digite uma opção: '))
    print('----------------------------------------------------------------------')
    if opc == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}.')
        print('----------------------------------------------------------------------')
    elif opc == 2:
        produto = n1*n2
        print(f'o produto de {n1} e {n2} é {produto}.')
        print('----------------------------------------------------------------------')
    elif opc == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print(f'O {maior} é maior que o {menor}.')
            print('----------------------------------------------------------------------')
        elif n2 > n1:
            maior = n2
            menor = n1
            print(f'O {maior} é maior que o {menor}.')
            print('----------------------------------------------------------------------')
        else:
            print(f'Os doi números são iguais.')
            print('----------------------------------------------------------------------')
    elif opc == 4:
        print('Digite novos números:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('----------------------------------------------------------------------')
    elif opc == 5:
        print('Finalizando...')
        print('----------------------------------------------------------------------')
    else:
        print('Opção invalida. Tente novamente.')
        print('----------------------------------------------------------------------')