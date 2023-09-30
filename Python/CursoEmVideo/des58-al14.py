''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa devera escrever na tela se o usuário venceu ou perdeu.'''
print('----------------------------------------------------------------------')
print('            J O G O  DE  A D I V I N H A Ç Ã O  DE N Ú M E R O S')
print('----------------------------------------------------------------------')
print('')
import random
r = 'n'
while r not in 'N':
    t = 1
    ns =  random.randint(0,5)
    c = int(input('Estou pensando em um numero de 0 a 5 qual é? '))
    while c != ns:
        c = int(input('Errou. Tente outro numero: '))
        t += 1
    print('----------------------------------------------------------------------')
    print(f'Acertou!!! Eu estava pensando no número {ns}.')
    print(f'Você precisou de {t} tentativas.')
    print('----------------------------------------------------------------------')
    r = str(input('Gostaria de jogar novamente? [S/N] ')).upper().strip()[0]
    print('----------------------------------------------------------------------')
    while r not in 'SN':
        r = str(input('Escolha uma opção valida. Gostaria de jogar novamente? [S/N] ')).upper().strip()[0]
