Algoritmo "EX-29-Aum-Sal"

Var
   t : inteiro
   as, ns, a: Real
   n, q : caractere

Inicio
      Escreval ("--------------------------------------------")
      Escreval ("           CALCULADORA DE SALARIO")
      Escreval ("--------------------------------------------")
      Escreval ("")
      Enquanto (q <> "n") faca
             Escreva ("Nome do funcionario(a): ")
             Leia (n)
             Escreva ("Tempo de serviço [anos]: ")
             Leia (t)
             Escreva ("Sálario atual: R$")
             Leia (as)
             Escreval ("")
             Escreval ("--------------------------------------------")
             Escreval ("")
             Se (t < 3) Entao
                a <- 3
                ns <- ((as / 100) * a) + as
             SeNao
                  Se  (t >= 3) e (t < 10) Entao
                      a <- 12.5
                      ns <- (((as / 100) * a) + as)
                  SeNao
                      a <- (20)
                      ns <- ((as / 100) * a) + as
                  FimSe
             FimSe
             Escreval ("Nome: ",n)
             Escreval ("Tempo de Serviço: ",t)
             Escreval ("Sálario atual: R$",as:4:2)
             Escreval ("Aumento: ",a,"%")
             Escreval ("Novo Sálario: R$",ns:4:2)
             Escreval ("")
             Escreva ("Gostaria de repetir a operação? [s/n]: ")
             Leia (q)
             Escreval ("--------------------------------------------")
             Escreval ("")
      FimEnquanto



Fimalgoritmo