Algoritmo "conteAte--"

var
   fimcontador,salto, contador : Inteiro
inicio
      Escreva("Ate quanto você quer que seja contado? ")
                   Leia (fimcontador)
      Escreva("De quanto em quanto você quer que seja contado? ")
                  Leia (salto)
      contador <- 0
      Enquanto  (contador <= fimcontador) faca
                Escreval (contador)
                contador <- contador + salto
      FimEnquanto
      Escreval("Terminei de contar!")

fimalgoritmo