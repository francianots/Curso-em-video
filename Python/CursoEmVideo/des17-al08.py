''#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
print("------------------------------------------------------")
print("    C A L C U L A D O R A DE H I P O T E N U S A")
print("------------------------------------------------------")
print("")
opos = float(input("Digite o comprimento do cateto oposto: "))
adja = float(input("Digite o comprimento do cateto ajacente: "))
hipotenusa = hypot(opos,adja)
print("")
print("------------------------------------------------------")
print(f"O valor da hipotenusa é: {hipotenusa:.2}")