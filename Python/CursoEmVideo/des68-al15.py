print('--------------------------------------------------------------------')
print('                    I M P A R   OU   P A R')
print('--------------------------------------------------------------------')
import random
rmaquina = rusuario = 0
while rmaquina =< 3 or rusuario =< 3:
    n = int(input('Digite um numero: '))
    escolha = str(input('Escolha impar ou par [I/P]: ')).strip().upper()[0]
    maquina = (random.randint(0,10))
    en = n%2
    emaquina = maquina%2
    if en > emaquina and escolha == 'I':
        print('Você ganhou!')
        rusuario += 1
    elif en < emaquina and escolha == 'P':
        print('Você ganhou!')
        rusuario += 1
    else:
        print('Você perdeu')
        rmaquina += 1
        print('----------------------------------------------')
    print(f'Maquina escolheu: {maquina}')
    print(f'Você escolheu: {n}')
    print('Placar')
    print (f'você {rusuario} X {rmaquina} maquina')



print('--------------------------------------------------------------------')