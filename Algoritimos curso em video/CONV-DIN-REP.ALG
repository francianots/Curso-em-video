Algoritmo "Conv-din-rep"


Var
   c, q : Inteiro
   r,d,eu: real

Inicio
      c<-0
      Escreval("---------------------------------------------------------")
      Escreval("                   CONVERSOR DE MOEDAS")
      Escreval("---------------------------------------------------------")
      Escreva("Quantas vezes voce gostaria de fazer a conversão? ")
      Leia (q)
      Enquanto (c<q) faca
              escreva ("Digite a quantos reais você tem? R$")
              leia (r)
              d<-r/4,85
              eu<-r/5,45
              escreval ("Com R$",r,",00 você consegue comprar:")
              escreval ("US$",d:4:2)
              escreval("OU")
              escreval ("€",eu:4:2)
              Escreval("")
              Escreval("")
              c<- c+1
       FimEnquanto
Fimalgoritmo