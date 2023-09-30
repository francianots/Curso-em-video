'''Crie um programa que leia o nome de uma cidade
 e diga se ela começa ou não com o nome "SANTO".'''

print('-------------------------------------------------------')
cidade = str(input('Digite o nome de uma cidade: '))
print('-------------------------------------------------------')
print('')
cidade = cidade.title()
inicio = (cidade.find('Santo'))
print(f'Nome da cidade: {cidade}')
print(f'o nome da cidade começa com Santo: {inicio == 0}')
