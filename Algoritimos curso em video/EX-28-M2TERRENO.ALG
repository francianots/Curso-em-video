Algoritmo "EX-28-m2terreno"

Var
   c, l, a : Real
   q : caractere

Inicio
      Escreval ("--------------------------------------------")
      Escreval ("                M² TERRENO")
      Escreval ("--------------------------------------------")
      Escreval ("")
      Enquanto (q <> "n") faca
             Escreva ("Digite o comprimeno [m]: ")
             Leia (c)
             Escreva ("Digite a largura [m]: ")
             Leia (l)
             Escreval ("")
             a <- (c * l)
             Escreval ("COMPRIMENTO: ",c,"m")
             Escreval ("LARGURA: ",l,"m")
             Escreval ("ÁREA: ",a,"m")
             Se (a < 100) Entao
                Escreval ("CATEGORIA: TERRENO POPULAR")
             SeNao
                  Se  (a > 99) e(a < 501) Entao
                      Escreval ("CATEGORIA: TERRENO MASTER")
                  SeNao
                       Escreval ("CATEGORIA: TERRENO VIP")
                  FimSe
             FimSe

             Escreval ("")
             Escreva ("Gostaria de repetir? [s/n]: ")
             Leia (q)
             Escreval ("--------------------------------------------")
             Escreval ("")
      FimEnquanto



Fimalgoritmo