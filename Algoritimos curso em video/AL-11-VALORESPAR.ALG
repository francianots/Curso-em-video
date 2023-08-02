Algoritmo "AL-11-ValoresPar"

Var
   c , v, p : Inteiro
   l : caractere
   
Inicio
    Enquanto l <> "n" faca
       Escreva ("Digite um número para o final da contagem: ")
       Leia (v)
       Escreva ("Digite um número do salto: ")
       Leia (p)
       Se (v% = 0) entao
       v <- v-1
       FimSe
       Para c <- 0 ate v  passo p faca
       Escreval (c)
       FimPara
       Escreva ("Gostaria de continuar? ")
       leia (l)
    FimEnquanto
Fimalgoritmo