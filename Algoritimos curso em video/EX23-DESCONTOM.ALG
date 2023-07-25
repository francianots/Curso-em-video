Algoritmo "EX23-DescontoM"

Var
   c,d: inteiro
   cd,ec: real
   n,s: caractere
Inicio
      Escreval("--------------------------------------")
      Escreval("               VIAGENS")
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("")
      Escreval("--------------------------------------")
      Escreva("Informe o seu nome: ")
                       Leia(n)
      Escreva("Qual : ")
                       Leia(s)
      Escreva("Informe o valor da sua compra: R$")
                       Leia(c)
      se (s="m")   entao
              d<-5
      Senao
           Se (s="f") entao
           d<-13
           Senao
                Escreval("SEXO INVALIDO")
           Fimse
      Fimse
      cd<-c-(c*d/100)
      ec<- c-cd
      
      Escreval("--------------------------------------")
      Escreval("")
      Escreval("")
      Escreval("--------------------------------------")
      Escreval("NOME: ",n)
      Escreval("SEXO: ",s)
      Escreval("VALOR DA COMPRA: R$",c:5:2)
      Escreval("VALOR DO DESCONTO: ",d,"%")
      Escreval("VALOR DA COMPRA COM DESCONTO: R$",cd:5:2)
      Escreval("VALOR ECONOMIZADO: R$",ec:5:2)
      Escreval("--------------------------------------")
Fimalgoritmo