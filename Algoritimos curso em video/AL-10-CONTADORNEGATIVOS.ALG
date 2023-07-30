Algoritmo "AL-10-contadorNegativos"

Var
   c,n, totN, s : inteiro
   resp : caractere
inicio
      Escreval ("-------------------------------------------------")
      Escreval ("              CONTADOR NEGATIVVOS")
      Escreval ("-------------------------------------------------")
      c <- 1
      Repita
            Escreva ("Escreva ", c,"°: ")
            leia (n)
            c <- c + 1
            Se (n < 0) entao
            totN <- totN + 1
            Fimse
      Ate (c=6)
      Escreval ("Total de números negativos: ",totN)
fimalgoritmo