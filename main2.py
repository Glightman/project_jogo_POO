from player import Steve
from relogio import Relogio
personagem = Steve()
relogio = Relogio()
dia = 1
def decor():
    print('-='*20)
print('-=-=-=-=- SEJA BEM VINDO AO "SIMULADOR DE VIDA" -=-=-=-=-')
decor()
print("São "+str(relogio)+" do dia "+str(dia)+". ")
print('''AJUDE O STEVE A TOMAR DECISÕES EM SEU DIA DIA.
-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
ESSAS SÃO AS SUAS ATRIBUÍÇÕES INICIAIS:
-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''')
decor()
print(personagem.dados())
mapa = int(input('''ACESSAR MAPA PARA INICIAR O JOGO?
[ 1 ] SIM
[ 0 ] NÃO (sair)
--> : '''))
while True:
    if mapa == 1 :
        opcao = int(input('''ESTES SÃO SEUS AMBIENTES:
        [ 1 ]  CASA
        [ 2 ]  BAR
        [ 3 ]  MERCADO
        [ 4 ]  ESCOLA
        [ 5 ]  RESTAURANTE
        [ 6 ]  TRABALHO
        [ 7 ]  ACADEMIA
        [ 0 ]  SAIR
        --> : '''))
        if opcao == 0:
            decor()
            print('VOCÊ SAIU DO JOGO')
            decor()
            break
        if opcao == 1:
            personagem.casa()
               
            
    
