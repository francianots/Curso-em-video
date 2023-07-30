Algoritmo "AL-10-numeros primos"

Var
   n, c, di : Inteiro
   r : caractere

Inicio
  Repita
      Escreval ("------------------------------------------------------")
      Escreval ("            IDENTIFICADOR DE NÚMEROS PRIMOS")
      Escreval ("------------------------------------------------------")
      Escreval ("")
      Escreva ("Digite um numero: ")
      leia (n)
      c <- 1
      Repita
            Se (n % c = 0) Entao
               di <- di + 1
            FimSe
            c <- c + 1
      ate (c > n)
      Se (di > 2) Entao
            Escreval ("O número ", n, " não é primo.")
      SeNao
            Escreval("O número ", n, " é primo")
      FimSe
      Escreva ("Gostaria de repetir a operação? [s/n]: ")
      leia (r)
      se (r <> "n") Entao
         Limpatela
      FimSe
    Ate r = "n"
Fimalgoritmo