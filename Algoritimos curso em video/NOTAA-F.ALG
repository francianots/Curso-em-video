Algoritmo "NotaA-F"

Var
   N1,N2, M : real
   Clas : caractere

Inicio

      Escreval ("--------------------------------")
      Escreval ("           NOTA FINAL")
      Escreval ("--------------------------------")
      Escreval("")
      Escreval("")
      Escreval ("--------------------------------")
      Escreva("    Digite sua primeira nota. ")
                    Leia (N1)
      Escreva("    Digite sua segunda nota. ")
                    Leia (N2)
      Escreval ("--------------------------------")
      Escreval("")
      Escreval("")
      M<- (N1+N2)/2
      Se (M<5) entao
         Clas<- "F"
      SeNao
           Se   (M>=5) e(M<=5.9) entao
                Clas<-"E"
           SeNao
                Se (M>=6) e(M<=6.9) Entao
                 Clas<-"D"
                 SeNao
                      Se (M>=7) e (M<=7.9) Entao
                         Clas<- "C"
                      SeNao
                           Se   (M>=8) e(M<=8.9) Entao
                                Clas<-"B"
                           SeNao
                                Se   (M>=9) entao
                                     Clas<-"A"
                                FimSe
                           FimSe
                      FimSe
                FimSe
           FimSe
      Fimse
      Escreval ("--------------------------------")
      Escreval ("         Media: ",M:2:1)
      Escreval ("          Nota: ",Clas)
      Escreval ("--------------------------------")
      
      
Fimalgoritmo