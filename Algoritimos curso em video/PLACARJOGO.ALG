Algoritmo "PlacarJogo"

Var
   t1,t2: caractere
   gt1,gt2: inteiro

Inicio
      Escreval("-----------------------------")
      Escreval("      PLACAR DO JOGO")
      Escreval("-----------------------------")
      Escreval("")
      Escreval("-----------------------------")
      Escreva("Qual o Time 1? ")
                     Leia(t1)
      Escreva("Quantos gols ele fez? ")
                       Leia(gt1)
      Escreval("-----------------------------")
      Escreva("Qual o Time 2? ")
                     Leia(t2)
      Escreva("Quantos gols ele fez? ")
                     Leia (gt2)
      Escreval("-----------------------------")
      Escreval("")
      Escreval(t1," ",gt1," X",gt2," ",t2)
      Escreval("-----------------------------")
      Se (gt1>gt2) e (gt1>5) entao
         Escreval (t1," GANHOU DE GOLEADA!!!")
      SeNao
           Se (gt1>gt2) entao
              Escreval(t1" GANHOU!!!")
           SeNao
                Se (gt2>gt1) e (gt2>5) entao
                   Escreval(t2" GANHOU DE GOLEADA!!!")
                SeNao
                     Se (gt2>gt1) entao
                        Escreval (t2" GANHOU!!!")
                     SeNao
                          Escreval ("  EMPATE")
                     FimSe
                FimSe
           FimSe

      Fimse


Fimalgoritmo