'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletimcontendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente.'''
alunos = []
qA = int(input('Quantos alunos você quer cadastrar?: '))
for c in range(qA):
    print('-=' * 10, f'{c+1}° ALUNO', '=-' * 10) 
    alunos.append([
        input('Nome: '),
        [float(input('Nota 1: ')),
        float(input('Nota 2: '))]
    ])
    alunos[c].append((alunos[c][1][0]+alunos[c][1][1])/2)
    print('-' * 50)
print(f'No.    {"NOME":<15}{"MEDIA":>12}')
print('-' * 50)
for i, c in enumerate(alunos):
    print(f'{i}      {c[0]:<15}', f'{c[2] :>10.2f}')
print('-' * 50)
while True:
    resp = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if resp == 999:
        break
    elif resp <= len(alunos):
        print(f'Notas de {alunos[resp][0]} são {alunos[resp][1]}')
        print('-' * 50)