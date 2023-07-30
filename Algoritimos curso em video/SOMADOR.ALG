Algoritmo "Somador"

var
   cont, n, s, ma, me : inteiro


inicio
      cont <- 1
      s <- 0
      n<-100000
      Enquanto (cont<=5) faca
                 Escreva("Digite o ",cont,"° Valor: ")
                 Leia (n)
                 Se (n > ma) entao
                    ma <- n
                 FimSe
                 Se (n<me) ou (me=0) entao
                      me <- n
                 FimSe
                 s<- s + n
                 cont <- cont + 1
      FimEnquanto
      Escreval("A soma total dos numeros foi: ",s )
      Escreval("O maior numero informado foi: ",ma)
      Escreval("O menor numero informado foi: ",me)
fimalgoritmo