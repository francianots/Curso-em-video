'''Faça um programa que ajudo um jogar da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''
import random
lista = []
jogos = []
print('-'*50)
print(f'{"JOGO DA MEGA SENA":^50}')
print('-'*50)
qJ = int(input('Quantos jogos você quer que eu sortei?: '))
print('-'*50)
print('-=' * 6, f'   SORTEANDO {qJ} JOGOS   ', '=-' * 6)
for c in range(qJ):
    cont = 0
    while True:
        n = random.randint(1,60)
        if n not in lista:
            lista.append(n)  
            cont += 1
        if cont == 6:
            lista.sort()
            jogos.append(lista[:])
            lista.clear()
            break
for c in range(qJ):
    print(f'jogo {c+1}: {jogos[c]}')
