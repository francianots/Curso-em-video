Algoritmo "EX17-Radar"

Var
   v,m: inteiro

Inicio
      Escreval("-----------------------------------------")
      Escreval("            RADAR DE VELOCIDADE")
      Escreval("-----------------------------------------")
      Escreva("Qual sua velocidade? ")
                    Leia(v)
      m<- (v-80)*5
      Se  (v>80) entao
      
          Escreval ("")
          Escreval("-----------------------------------------")
          Escreval ("Você ultrapassou o limite de velocidade.")
          Escreval ("Multa: R$",m)
          Escreval("-----------------------------------------")
      SeNao
           Escreval ("")
           Escreval("-----------------------------------------")
           Escreval("Você esta dentro do limite de velocidade.")
           Escreval("-----------------------------------------")
      Fimse

Fimalgoritmo