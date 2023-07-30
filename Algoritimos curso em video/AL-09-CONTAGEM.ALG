Algoritmo "AL-09-Contagem"


Var
   i, f : Inteiro
Inicio
      Escreval("---------------------------------------------------------")
      Escreval("                        CONTADOR")
      Escreval("---------------------------------------------------------")
      Escreva("Inicio da contagem: ")
      Leia (i)
      Escreva("Fim da contagem: ")
      Leia (f)
      Escreval("---------------------------------------------------------")
      Enquanto (i<>f) Faca
               Se (i<f) Entao
               Escreva (i,"... ")
                  i <- i+1
               SeNao
                    Escreva (i,"... ")
                    i <- i-1
               FimSe

       FimEnquanto
       Escreval("---------------------------------------------------------")
Fimalgoritmo