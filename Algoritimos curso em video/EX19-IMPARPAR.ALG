Algoritmo "EX21-bissexto"

Var
   ano: inteiro
   bi: caractere
Inicio
      Escreval("--------------------------------------")
      Escreval("              ANO BISSEXTO")
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("")
      Escreval("--------------------------------------")
      Escreva("Informe o ano. ")
                       Leia(ano)
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("")

      Se (ano%4=0) entao
         bi<- "bissexto"
      Senao
           bi<- "normal"
      Fimse
      Escreval("--------------------------------------")
      Escreval("O ano de",ano," é ",bi,".")
      Escreval("--------------------------------------")

Fimalgoritmo