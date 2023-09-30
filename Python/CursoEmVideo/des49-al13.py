'''Faça uma tabuada de um número escolhido pelo o úsuario.'''
print('----------------------------------------------------------------------')
print('                          T A B O A D A')
print('----------------------------------------------------------------------')
print('')
t = int(input('Digite um número: '))
for c in range (1,11):
    print(f'{t} X {c} = {t*c}')
print('')
print('----------------------------------------------------------------------')
