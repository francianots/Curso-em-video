Algoritmo "MediaNota"


Var
   N1,N2,M: real

Inicio
      Escreval ("--------------------------")
      Escreval ("   ESCOLA PARA BURROS")
      Escreval ("--------------------------")
      Escreva ("Primeira Nota: ")
               Leia (N1)
      Escreva ("Segunda Nota: ")
               Leia (N2)
      M <- (N1+N2)/2
      Escreval ("")
      Escreval ("---------STATUS----------")
      Escreval ("        MÉDIA:",M:4:2)
      Se (M >= 7) entao
         Escreval ("        APROVADO")
         SeNao
         Se (M>=5) e (M<7) entao
            Escreval ("       RECUPERAÇÃO")
         SeNao
            Escreval ("       REPROVADO")
         Fimse


      FimSe
      Escreval ("--------------------------")
      

Fimalgoritmo
