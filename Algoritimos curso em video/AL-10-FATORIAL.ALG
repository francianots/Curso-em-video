Algoritmo "AL-10-fatorial"

Var
   n, C, f : Inteiro
   r : caractere
inicio
  Repita
      Escreval ("-----------------------------------------------")
      Escreval ("                   FATOTIAL")
      Escreval ("-----------------------------------------------")
      Escreval ("")
      Escreva ("Digite um número: ")
      Leia (n)
      c <- n
      f <- 1
      Repita
            f<- f * n
            c <- c - 1
      Ate (c < 1)
      Escreval ("O valor fatorial de ", n , " e igual a ", f )
      Escreva ("Quer continuar? [s/n] :")
      Leia (r)
      Limpatela
  Ate (r = "n")
fimalgoritmo