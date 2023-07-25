Algoritmo "dEPENDENTESfUNCIONARIO"

Var
   Nome: caractere
   sal, nsal, dep : real

Inicio
      Escreva ("Qual o seu nome? ")
               leia (nome)
      Escreva ("Qual o seu salario atual? R$")
               Leia (sal)
      Escreva ("Quantos depentendes você tem? ")
               Leia (dep)
      Escolha dep
              Caso0
                   nsal<- sal+(sal*5/100)
              Caso 1,2,3
                   nsal<- sal+(sal*10/100)
              Caso 4,5,6
                   nsal<- sal+(sal*15/100)
              Outrocaso
                   nsal<- sal+(sal*20/100)
      Fimescolha
      Escreva(nome," seu novo salario é de: R$", nsal:5:2)

Fimalgoritmo