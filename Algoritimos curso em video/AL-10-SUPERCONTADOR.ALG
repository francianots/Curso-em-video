Algoritmo "AL-10-Supercontador"

Var
     i, c, me, he :inteiro
     op, s : caractere

Inicio
      Repita
            Escreval ("----------------------------------------")
            Escreval ("          CONTADOR DE PESSOAS")
            Escreval ("----------------------------------------")
            Escreval ("")
            Escreva ("Qual o sexo? [m/f] ")
            Leia (s)
            Escreva ("Qual a idade? ")
            Leia (i)
            Escreval ("----------------------------------------")
            Escreval ("Qual a cor do cabelo? ")
            Escreval ("[1] Preto")
            Escreval ("[2] Castanho")
            Escreval ("[3] Loiro")
            Escreval ("[4] Ruivo")
            Escreval ("")
            Leia (c)
            Se (s = "f") e (i > 24)e (i < 31) e (c = 3) Entao
               me <- me + 1
            FimSe
            Se ( s = "m") e (i > 18) e (c = 2) Entao
               he <- he +1
            FimSe
            Escreva ("Quer continuar? [s/n] ")
            Leia (op)
            Se (op <> "s") ou (op <> "n" ) entao
               Escreval ("**ESCOLHA UMA OPÇÃO VALIDA!**")
               Escreva ("Quer continuar? [s/n]: ")
      Ate (op = "n")
      Escreval ("O total de homens maiores de 18 anos com o cabelo castanho é: ",he)
      Escreval ("O total de mulheres loiras entre 25 e 30 anos é: ", me)


Fimalgoritmo