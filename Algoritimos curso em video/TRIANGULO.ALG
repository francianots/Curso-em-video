Algoritmo "triangulo"

var
    L1,L2,L3: inteiro
    eq, es, tri: logico
inicio
      escreva ("Digite o primeiro lado: ")
              Leia   (L1)
      escreva ("Digite o segundo lado: ")
              Leia (L2)
      Escreva ("Digite o terceiro lado: ")
              Leia (L3)
      tri<- (L1<L2 +L3) e (L2< L1+L3) e (L3< L1+L2)
      eq <-(L1=L2) e  (L2= L3)
      es <-(L1<>L2) e (L2<>L3) e (L1<>L3)
      escreval ("Pode formar um triangulo? ", tri)
      escreval ("O triangulo e EQUILATERO? ",  EQ)
      escreval ("O triangulo e ESCALENO? " , es)
fimalgoritmo