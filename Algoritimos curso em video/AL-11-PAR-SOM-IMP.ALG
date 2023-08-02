Algoritmo "AL-11-par-som-imp"

Var
   c, v, t, si : Inteiro
Inicio
   t <- 0
   Para c <- 1 ate 6 faca
        Escreva ("Digite um número: ")
        Leia (v)
        Se (V % 2 = 1) Entao
           si <- (si + v)
        Fimse
        Se (v >= 0) e (v <= 10) Entao
           t <- t + 1
        FimSe
   FimPara
   Escreval ("O total de número entre 0 e 10 é: ",t)
   Escreval ("A soma de todos os numeros impar é : ", si)
Fimalgoritmo