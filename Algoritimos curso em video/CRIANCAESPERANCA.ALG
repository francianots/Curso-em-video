Algoritmo "CriancaEsperanca"

Var
      D: inteiro
      Valor : real
Inicio
      Escreval("-------------------------------")
      Escreval("       CRIANÇA ESPERANÇA       ")
      Escreval("-------------------------------")
      Escreval("   Muito obrigado por ajudar!  ")
      Escreval(" [1] para doar R$10,00 ")
      Escreval(" [2] para doar R$25,00 ")
      Escreval(" [3] para doar R$50,00 ")
      Escreval(" [4] para doar outros valores ")
      Escreval(" [5] para cancelar ")
      Leia (D)
      Escolha D
              Caso 1
                   Valor <-10
              Caso 2
                   Valor <-25
              Caso 3
                   Valor <-50
              Caso 4
                   Escreval ("Qual o valor que gostaria de doar? ")
                   leia (Valor)
              Caso 5
                   Valor <-0
      FimEscolha
      Escreval("-------------------------------")
      Escreval ("        DOAÇÃO: R$",valor:4:2)
      Escreval ("      OBRIGADO POR DOAR!")
      Escreval("-------------------------------")

Fimalgoritmo