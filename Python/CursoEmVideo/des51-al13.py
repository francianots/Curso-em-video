'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA no final,
 mostre os 10 primeiros termos dessa progressão. '''
print('----------------------------------------------------------------------')
print('                  10  T E R M O S  DE  U M A   PA')
print('----------------------------------------------------------------------')
print('')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro,decimo + razao,razao):
    print (c, end=' → ')
print('ACABOU')
print('')
print('----------------------------------------------------------------------')
