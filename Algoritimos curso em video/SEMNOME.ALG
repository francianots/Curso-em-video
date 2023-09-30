Algoritmo "semnome"

Var
   Alt, Peso, IMC : Real
   Nome, R : caractere

procedimento calc (var a, b, c : real)
Var
Peso, Alt, IMC : Real
Inicio
   c <- (a/b**2)
FimProcedimento
Inicio
      Enquanto (R <> "n") faca
               LimpaTela
               Escreval ("---------------------------------------------------------")
               Escreval ("        I N D I C E  DE M A S S A  C O R P O R I A")
               Escreval ("---------------------------------------------------------")
               Escreva ("Digite seu nome: ")
               Leia (Nome)
               Escreva ("Digite sua altura: ")
               Leia (Alt)
               Escreva ("Digite seu peso: ")
               Leia (Peso)
               IMC <- 0
               calc (Peso, Alt, IMC)
               IMC >18
               Escreval ("")
               Escreval ("")
               Escreval ("---------------------------------------------------------")
               Escreval ("Nome: ", Nome)
               Escreval ("Peso: ", Peso)
               Escreval ("Altura: ", Alt)
               Escreval ("IMC: ", IMC)
               Escreval ("---------------------------------------------------------")
               Escreval ("")
               Escreva ("Gostaria de continuar? [s/n]: ")
               Leia (R)
      FimEnquanto
               
Fimalgoritmo