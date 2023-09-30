'''Desenvoçva um programa que leia o nome, idade e sexo de 4 pessoas.
Nofinal do programa, mostre:
-A média de idade do grupo.
-Qual é o nome do homem mais velho.
-Quantas Mulheres têm menos de 20 anos.'''
print('----------------------------------------------------------------------')
print('              C A T A L A G O L A D O R  DE  P E S S O A S')
print('----------------------------------------------------------------------')
print('')
mm = 0
hm = 0
mi = 0
for c in range (1,5):
    print(f'{c}ª pessoa.')
    n = input('Digite o nome: ')
    s = input('Digite o sexo: [m/f] ')
    i = int(input('Digite a idade: '))
    mi += i
    if i < 20 and s == 'f':
        mm += 1
    if i > hm:
        hm = i
        nhm = n
print('')
print('----------------------------------------------------------------------')
print(f'A média de idade é de {mi/4:.0f} anos.')
print(f'O homem mais velho é {nhm} com {hm} anos.')
print(f'O total de pessoas do sexo feminino com menos de 20 anos é de {mm}.')
print('----------------------------------------------------------------------')