Algoritmo "CalcImc"

Var
   massa, altura, imc: real
Inicio
      Escreva ("Qual o seu peso? (Kg): ")
              Leia (massa)
      Escreva ("Qual a sua altura? (m): ")
              Leia (altura)
      imc <- massa/(altura^2)
      Escreval ("Seu IMC é de ", imc:5:2)
      Se (imc<17) Entao
         Escreval ("Muito abaixo do peso.")
      Senao
           Se (imc>=17) e (imc<=18.5) entao
              Escreval ("Abaixo do peso.")
           Senao
                Se (imc>18.5) e (imc<=25) entao
                   Escreval ("Peso ideal.")
                Senao
                     Se   (imc>25) e(imc<=30) entao
                          Escreval ("Sobrepeso.")
                     Senao
                          Se   (imc>30) e (imc<=35) entao
                               Escreval("Obesidade.")
                          Senao
                               Se   (imc>35) e (imc<=40) entao
                                    Escreval ("Obesidade Severa.")
                               Senao
                                    Escreval("Obesidade Mórbida")
                               Fimse
                          Fimse
                     Fimse
                
                Fimse
           Fimse
      Fimse


Fimalgoritmo