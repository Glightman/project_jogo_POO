from player import Steve
from relogio import Relogio
personagem = Steve()
relogio = Relogio()
dia = ''


def decor():
    print('-='*30)
decor()
print('-=-=-=-=- \033[1m\033[33mSEJA BEM VINDO AO "SIMULADOR DE VIDA"\033[04;37m -=-=-=-=-')
decor()
print("São "+str(relogio)+". ")
print('AJUDE O STEVE A TOMAR DECISÕES EM SEU DIA DIA.')
decor()
print('ESSAS SÃO AS SUAS ATRIBUÍÇÕES INICIAIS:')
print(personagem.dados())
mapa = int(input('''ACESSAR MAPA PARA INICIAR O JOGO?
[ 1 ] SIM
[ 0 ] NÃO (sair)
--> : '''))
if mapa == 1:
    personagem.map()
   
        
      
               
            
    
