'''Crie um origrama onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionario. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
}
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
raking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
print(f'{"=-"*5:<10}', f'{"RANKING":^10}', f'{"-="*5:>10}')
for i, v in enumerate(raking):
    print(f'O {i+1}° colocado: {v[0]} tirou {v[1]}')
    sleep(1)