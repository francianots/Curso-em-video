Algoritmo "AL-11-Seq-fibonacci"
Var
   c, f1, f2 : Inteiro
   q : Caractere
Inicio
      Enquanto (q <> "n") Faca
               f1 <- 1
               f2 <- 0
               Escreval (0)
               Para c <- 1 ate 7 faca
                    f1 <- (f1 + f2)
                    Escreval (f1)
                    f2 <- (f2 + f1)
                    Escreval (f2)
               Fimpara
               Escreva ("Gostaria de continuar? ")
               Leia (q)
      Fimenquanto
Fimalgoritmo