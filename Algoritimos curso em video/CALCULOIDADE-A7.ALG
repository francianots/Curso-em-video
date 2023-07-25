Algoritmo "CalculoIdade-a7"


Var
   ano, nasc, idade : inteiro

Inicio
      Escreva ("Em que ano estamos?")
      Leia (ano)
      Escreva ("Em que ano você nasceu?")
      Leia (nasc)
      idade<- ano-nasc
      Escreva ("Em",ano," você tera ", idade, " anos ")
      Se (idade >= 21) entao
         Escreva ("e ja tera atingido a maior idade.")
      SeNao
           Escreva ("e é menor de idade.")
      Fimse

Fimalgoritmo