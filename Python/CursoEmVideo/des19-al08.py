# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro.
# Faça um programa que ajude ele. lendo o nome deles
# e escrevendo o nome do escolhido.

import secrets
al1 = input("Digite o nome do primeiro aluno: ")
al2 = input("Digite o nome do segundo aluno: ")
al3 = input("Digite o nome do terceriro aluno: ")
al4 = input("Digite o nome do quarto aluno: ")
qua = [al1,al2,al3,al4]
print ("Quem limpara o quadro seá: ",secrets.SystemRandom().choice(qua))
