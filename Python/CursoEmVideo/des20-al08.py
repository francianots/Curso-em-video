# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
print("------------------------------------------------")
print("      S O R T E I O DE A L U N O S")
print("------------------------------------------------")
print("")
al1 = input("Digite o nome do primeiro aluno: ")
al2 = input("Digite o nome do segundo aluno: ")
al3 = input("Digite o nome do terceiro aluno: ")
al4 = input("Digite o nome do quarto aluno: ")
tra = al1, al2, al3, al4
c = 4
print("")
print("------------------------------------------------")
print("A sequencia de apresentação do trabalho sera a seguinte:", random.SystemRandom().sample(tra,c))
print("------------------------------------------------")