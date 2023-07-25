Algoritmo "Creuza_Emprestimo"


Var
valor_emprestimo, qtd_parcelas, valor_parcelas, total_emprestimo: real

Inicio
        escreva("Qual o valor do emprestimo?")
        leia (valor_emprestimo)
        escreva("Qual a quantidade de parcelas?")
        leia (qtd_parcelas)
        total_emprestimo<- ((valor_emprestimo*20)/100)+valor_emprestimo
        valor_parcelas <- total_emprestimo/qtd_parcelas
        escreva("O valor total do emprestimo é R$", total_emprestimo:5:2, " em", qtd_parcelas, "X de R$", valor_parcelas:5:2)

        
Fimalgoritmo