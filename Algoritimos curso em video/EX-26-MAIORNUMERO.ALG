Algoritmo "EX-26-MaiorNumero"

Var
   n1, n2 : Inteiro
   q : caractere

Inicio
      Escreval ("--------------------------------------------")
      Escreval ("                MAIOR NÚMERO")
      Escreval ("--------------------------------------------")
      Escreval ("")
    Enquanto (q <> "n") faca
      Escreva ("Digite 1° número: ")
      Leia (n1)
      Escreva ("Digite 2° número: ")
      Leia (n2)
      Escreval ("")
      Se (n1 > n2) Entao
         Escreval ("O número ",n1," é maior que o",n2,".")
         SeNao
              Se  (n2 > n1) Entao
                  Escreval ("O número ",n2," é maior que o",n1,".")
              SeNao
                   Escreval ("O número ", n1, " é igual ao ",n2,".")
              FimSe
      FimSe
      Escreval ("--------------------------------------------")
      Escreval ("")
      Escreva ("Gostaria de repetir? [s/n]: ")
      Leia (q)
      Escreval ("")
    FimEnquanto



Fimalgoritmo