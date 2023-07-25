Algoritmo "EX24-precoCorrida"

var
   nome, destino: caractere
   km: inteiro
   preco: real


Inicio
      Escreval("--------------------------------------")
      Escreval("           PREÇO DA CORRIDA")
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("--------------------------------------")
      Escreva("Qual o seu nome? ")
                    Leia (nome)
      Escreva("Qual o seu destino? ")
                    Leia (destino)
      Escreva("Qual a distancia em km? ")
                    Leia (km)
      Se   (km<200) Entao
           preco<- km*0.5
      Senao
           preco<- km*0.45
      Fimse
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("--------------------------------------")
      Escreval("NOME:",nome)
      Escreval("DESTINO:",destino)
      Escreval("VALOR: R$",preco:4:2)
      Escreval("--------------------------------------")
      
      

Fimalgoritmo