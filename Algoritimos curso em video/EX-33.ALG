Algoritmo "Ex-33"

Var
   nome, c : Caractere
   valorImovel, valorEntrada, quantParc, valorFinan, valorParc, salario, juros : Real
Procedimento Tela()
Inicio
                 Escreval ("Status: APROVADO")
                 Escreval ("Valor da parcela: R$", valorParc:4:2)
                 Escreval ("Total de juros: ", juros, "%")
FimProcedimento
Inicio
      Enquanto (c <> "n") Faca
              LimpaTela
              Escreval ("-------------------------------------------------")
              Escreval (" S I M U L A D O R DE F I N A N C I A M E N T O")
              Escreval ("-------------------------------------------------")
              Escreval ("")
              Escreva ("Digite nome: ")
              Leia (nome)
              Escreva ("Digite salario: R$")
              Leia (salario)
              Escreva ("Digite o valor do imovel: R$")
              Leia (valorImovel)
              Escreva ("Digite o valor da entrada: R$")
              Leia (valorEntrada)
              Escreva ("Digite a quantidade de parcelas: ")
              Leia (QuantParc)
              Escreva ("digite o juros ao ano: %")
              Leia (juros)
              valorFinan <- valorImovel - valorEntrada
              juros <- (quantParc/12)*juros
              valorFinan <- (valorFinan/100)*juros + valorFinan
              valorParc <- valorFinan/quantParc
              Escreval ("")
              Escreval ("-------------------------------------------------")
              Escreval ("")
              Escreval ("Nome:", nome)
              Escreval ("Salario: R$", salario:4:2)
              Escreval ("Valor do Imovel: R$", valorImovel:4:2)
              Escreval ("Valor de entrada: R$", valorEntrada:4:2)
              Escreval ("Valor financiado: R$", valorFinan:4:2)
              Se (valorParc < ((salario/100)*30)) Entao
                 Tela()
              SeNao
                   Escreval ("Status: REPROVADO")
              Fimse
              Escreval ("Fazer nova simulação? [s/n]: ")
              Leia (c)
      FimEnquanto
Fimalgoritmo