'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
print('----------------------------------------------------------------------')
print('        I D E N T I F I C A D O R  DE  M A I O R I D A D E')
print('----------------------------------------------------------------------')
print('')
mi = 0
aa = int(input('Digite o ano atual yyyy: '))
for c in range(1,8):
    an = int(input(f'Digite o ano de nascimento da {c}ª pessoa yyyy: '))
    print(f'{aa-an} anos')
    if aa - an > 17:
        mi += 1
prin('')
print(f'{mi} pessoas são maiores de 18 anos.')