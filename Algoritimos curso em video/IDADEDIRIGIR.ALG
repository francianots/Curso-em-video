Algoritmo "IdadeDirigir"


Var
   AnoAtual, AnoNasc, Idade: inteiro

Inicio
      Escreval ("--------------------------")
      Escreval (" DEPARTAMENTO DE TRANSITO")
      Escreval ("--------------------------")
      Escreva ("Ano Atual (yyyy): ")
               Leia (AnoAtual)
      Escreva ("Ano de Nascimento (yyyy): ")
               Leia (anoNasc)
      Idade <- AnoAtual-AnoNasc
      Escreval ("")
      Escreval ("---------STATUS----------")
      Escreval ("     IDADE: ",Idade," ANOS")
      Se (idade >= 18) entao
         Escreval ("   APTO A TIRAR CARTEIRA")
      SeNao
         Escreval ("  INAPTO A TIRAR CARTEIRA")
      FimSe
      Escreval ("--------------------------")
      

Fimalgoritmo