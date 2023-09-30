'''Faça um programa que leia um número inteiro e
diga se ele é ou não um numero primo. '''
print('----------------------------------------------------------------------')
print('        I D E N T I F I C A D O R  DE  N Ú M E R O S  P R I M O S')
print('----------------------------------------------------------------------')
print('')
n = int(input('Digite um número: '))
cp = 1
for c in range (1,n):
    if n%c ==0:
        cp += 1
if cp > 2:
    print(f'O número {n} é divisivel por {cp} números. Por tanto não é primo.')
else:
    print(f'O número {n} é divisivel somente por {cp} números (ele mesmo e 1). Por tanto ele é um número primo')
    print('')
    print('----------------------------------------------------------------------')
