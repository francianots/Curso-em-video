'''Faça um programa que leia uma frase pelo teclado e mostre:

-Quantas vezes aparece a letra "a".
-Em que posição ela aparece a primeira vez.
-Em que posição ela aparece a última vez.'''
print('-----------------------------------------------')
frase = input('Digite uma frase:').lower()
print('-----------------------------------------------')
print('')
print(f'Nesta frase a letra "a" aparece {frase.count("a")} vezes.')
print(f'A letra "a" aparece pela 1° vez na posição: {frase.find("a")+1}')
print(f'A letra "a" aparece pela ultima vez na posição: {frase.rfind("a")-frase.count(" ")}')
print('-----------------------------------------------')