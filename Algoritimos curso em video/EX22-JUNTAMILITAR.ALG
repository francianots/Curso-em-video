Algoritmo "EX22-JuntaMilitar"

Var
   aa, an, i,if: inteiro
   s: caractere
Inicio
      Escreval("--------------------------------------")
      Escreval("             JUNTA MILITAR")
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("")
      Escreval("--------------------------------------")
      Escreva("Informe o ano atual: ")
                       Leia(aa)
      Escreva("Informe sua data de nascimento: ")
                        Leia (an)
      i<-aa-an
      Se (i>=18) entao
         s<-"APTO"
         if<-0
      Senao
           s<-"INAPTO"
           if<-18-i
           
      Fimse
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("")


      Escreval("--------------------------------------")
      Escreval("IDADE:",i)
      Escreval("SITUAÇÃO:",s)
      Escreval("VOLTE EM",if," ANOS")
      Escreval("--------------------------------------")

Fimalgoritmo