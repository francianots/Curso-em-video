Algoritmo "EX16-Cal-Fumo"


Var
cdia , anosfum, cfum : inteiro
tperd: real

Inicio
escreva ("Quantos cigarros por dia vocÊ fuma?")
leia (cdia)
escreva("A quantos anos você fuma?")
leia (anosfum)
cfum <- ((365*anosfum)*cdia)
tperd <- (cfum*10)\1440
escreva ("Neste periodo você ja fumou cerca de", cfum," cigarros e perdeu", tperd," dias de vida.")


Fimalgoritmo