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
if mapa == 1:
    personagem.opcao()
   
        
      
               
            
    
