'''
from player import Steve
from relogio import Relogio

if(__name__ == "__main__"): # Isso significa que se __name__ é igual a __main__ , o arquivo deve ser o arquivo principal e realmente estar em execução 
    dia = 1
    relogio = Relogio()
    personagem = Steve()
    personagem.dados()
    print(personagem)
        
    while True:
        print("---")
        print("São "+str(relogio)+" do dia "+str(dia)+". O que prefere fazer agora? ")
        print(personagem)
        opcao = int(input('''
        #Escolha sua ação:
        #Digite o número da ação desejada :
        #[1] - Higiene Pessoal
        #[2] - Tomar café da manhã
        #[3] - Beber água
        #[4] - Ir para a escola
        #[5] - Ir para academia
        #[6] - Ir ao mercado
        #[7] - Ir trabalhar
        #[0] - Sair do jogo
'''))
    
        if opcao == 1:
            relogio.avancaTempo(40)
            personagem.HigienePessoal()
            print(personagem.dados())
        elif opcao == 2:
            relogio.avancaTempo(35)
            personagem.Comer()
            personagem.comida()
            print(personagem.dados())
        elif opcao == 3:
            relogio.avancaTempo(5)
            personagem.Beber()
            print(personagem.dados())
        elif opcao == 4 :
            relogio.avancaTempo(300)
            personagem.Estudar()
            print(personagem.dados())
        elif opcao == 5:
            relogio.avancaTempo(85)
            personagem.Malhar()
            print(personagem.dados())
        elif opcao == 6:
            relogio.avancaTempo(60)
            personagem.Comprar()
            print(personagem.dados())
        elif opcao == 7:
            relogio.avancaTempo(515)
            personagem.Trabalhar()
            print(personagem.dados())
        elif opcao == 0:
            print('Fim do jogo')
            break
        else:  
            print("Opção inválida!")
            relogio.avancaTempo(3)
'''

from player import Steve
from relogio import Relogio

if(__name__ == "__main__"): # Isso significa que se __name__ é igual a __main__ , o arquivo deve ser o arquivo principal e realmente estar em execução 
    dia = 1
    relogio = Relogio()
    personagem = Steve()
    personagem.dados()
    print(personagem)
        
    while True:
        print("---")
        print("São "+str(relogio)+" do dia "+str(dia)+". O que prefere fazer agora? ")
        print(personagem)
        opcao = int(input('''
        Escolha sua ação:
        Digite o número da ação desejada :
        [1] - Higiene Pessoal
        [2] - Tomar café da manhã
        [3] - Beber água
        [4] - Ir para a escola
        [5] - Ir para academia
        [6] - Ir ao mercado
        [7] - Ir trabalhar
        [0] - Sair do jogo
        '''))
    
        if opcao == 1:
            relogio.avancaTempo(40)
            personagem.HigienePessoal()
            print(personagem.dados())
        elif opcao == 2:
           
            relogio.avancaTempo(35)
            personagem.Comer()
            print(personagem.dados())
                          
        elif opcao == 3:
            relogio.avancaTempo(5)
            personagem.Beber()
            print(personagem.dados())
        elif opcao == 4 :
            relogio.avancaTempo(300)
            personagem.Estudar()
            print(personagem.dados())
        elif opcao == 5:
            relogio.avancaTempo(85)
            personagem.Malhar()
            print(personagem.dados())
        elif opcao == 6:
            relogio.avancaTempo(60)
            personagem.Comprar()
            print(personagem.dados())
        elif opcao == 7:
            relogio.avancaTempo(515)
            personagem.Trabalhar()
            print(personagem.dados())
        elif opcao == 0:
            print('Fim do jogo')
            break
        else:  
            print("Opção inválida!")
            relogio.avancaTempo(3)

            



            