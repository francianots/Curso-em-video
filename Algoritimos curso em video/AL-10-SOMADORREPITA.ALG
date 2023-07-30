Algoritmo "AL-10-SomadorRepita"

Var
   n1, n2, s : inteiro
   resp : caractere
inicio
      Escreval ("-------------------------------------------------")
      Escreval ("                    SOMADOR")
      Escreval ("-------------------------------------------------")
      resp <- "s"
      Repita
               Escreva ("1° número: ")
               Leia (n1)
               Escreva ("2° número: ")
               Leia (n2)
               s <- n1 + n2
               Escreval ("A soma de",n1," com",n2," é:",s)
               Escreva ("Deseja fazer outra soma? [s/n]: ")
               Leia (resp)
               Escreval ("-------------------------------------------------")
               Escreval ("")
      Ate (resp = "n")
fimalgoritmo