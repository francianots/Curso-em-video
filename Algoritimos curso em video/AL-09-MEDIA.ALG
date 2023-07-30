Algoritmo "AL-09-media"


Var
   qa, q : Inteiro
   nt1, nt2, ntm, m_ntm: Real
   na, na_ntm : Caractere
Inicio
      Escreval("---------------------------------------------------------")
      Escreval("                    NOTAS DOS ALUNOS")
      Escreval("---------------------------------------------------------")
      Escreva("Quantidade de alunos: ")
      Leia (qa)
      q <- 0
      Escreval("---------------------------------------------------------")
      Enquanto (q < qa) Faca
               Escreva ("Nome do ",q +1,"° aluno: ")
               Leia (na)
               Escreva ("1° Nota: ")
               Leia (nt1)
               Escreva ("2° Nota: ")
               Leia(nt2)
               ntm <- (nt1+nt2)/2
               q <- q + 1
               Se (ntm > m_ntm) entao
                  m_ntm <- ntm
                  na_ntm <- na
               FimSe
               
               Escreval("---------------------------------------------------------")
      FimEnquanto
      Escreval ("")
      Escreval ("               ALUNO COM MAIOR NOTA MÉDIA")
      Escreval ("")
      Escreval ("Nome: ",na_ntm)
      Escreval ("Nota: ",m_ntm)
      Escreval("---------------------------------------------------------")
Fimalgoritmo
