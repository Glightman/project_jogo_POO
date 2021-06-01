from relogio import Relogio
from time import sleep
relogio = Relogio()

class Steve:
    def __init__(self):
        self.energia = 10 #NO ATRIBUTO ENERGIA ELE JA INICIA COM O MAX POIS ESSE É UM DOS ATRIBUTOS QUE VAI MANDAR NA VIDA DO PERSONAGEM
        self.fome = 5 #A FOME JA SE INICIA NA METADE POIS É O MOMENTO EM QUE O PERSONAGEM ACORDA. ESSE ATRIBUTO TAMBÉM CONTROLA A VIDA.
        self.sede = 5 #A SEDE JA SE INICIA NA METADE POIS É O MOMENTO EM QUE O PERSONAGEM ACORDA. ESSE ATRIBUTO TAMBÉM CONTROLA A VIDA.
        self.saúde = 10 #O ATRIBUTO SAÚDE TAMBÉM CONTROLA A VIDA E VAI DIMINUINDO EM ALGUMAS SITUAÇÕES.
        self.dinheiro = 0 #O ATRIBUTO DINHEIRO SERÁ USADO PARA FAZER COMPRAS DURANTE O JOGO.
        self.inteligência = 5
        self.comida = 10 #ESTE ATRIBUTO FUNCIONA COMO UM ESTOQUE DE SUPRIMENTOS RESPONSÁVEL PELA FOME E SEDE.
        self.remedio = 10 #ESTE ATRIBUTO FUNCIONA COMO UM ESTOQUE DE SUPRIMENTOS RESPONSÁVEL PELA SAÚDE.
        self.comprar = 10
     #AÇÕES ATRIBUÍDAS AO JOGADOR: ABAIXO NÓS TEMOS TODAS AS AÇÕES QUE O JOGADOR PODE FAZER EM CADA AMBIENTE.

    def dados(self): #ESSE MÉTODO MOSTRA OS ATRIBUTOS DO PERSONAGEM, ASSIM ELE PODE ACOMPANHAR SUA VIDA E TOMAR DECISÕES BASEADAS NESSAS INFORMAÇÕES.
        #NESTA LINHA ABIXO NÓS TEMOS UM PRINT DOS ATRIBUTOS, O CÓDIGO ANTES E DEPOIS DO TEMA SERVE PARA COLORIR O TEXTO QUE SERÁ MOSTRADO NO TERMINAL, ALÉM DE COLOCAR AS LETRAS EM NEGRITO TAMBÉM.
        #NÓS TAMBÉM USAMOS O f' PARA MOSTRAR OS ATRIBUTOS DIRETAMENTE DA VARIÁVEL.
        print(f"São "+str(relogio)+". ")
        print(f'''           \033[1m\033[33mSEUS ATRIBUTOS SÃO:\033[04;37m
        \033[1m\033[04;37m[ENERGIA      -->  {self.energia}/20]
        [SEDE         -->  {self.sede}/10]
        [FOME         -->  {self.fome}/10]
        [SAÚDE        -->  {self.saúde}/10]
        [DINHEIRO     -->  {self.dinheiro}]
        [INTELÍGÊNCIA -->  {self.inteligência}/10]
        [SUPRIMENTOS  -->  {self.comida}/ 10]
        [REMÉDIOS     -->  {self.remedio}/10]\033[04;37m''')
    
    def decor(self): #ESTA FUNÇÃO SERVE PARA DECORAR NOSSO TEXTO NO TERMINAL 
        print('-='*30) #ESSE PRINTE FARA UMA LINHA IGUAL A ESSA -->: -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def mostraAcao(self, acao):
        print('-=' * 40)
        string = f'Você está {acao}...'
        for ch in string:
            sleep(0.3)
            print(ch, end='', flush=True)
        print(' ')
        print('-=' * 40)
                
    def ler(self): #A FUNÇÃO LER OU AÇÃO LER, ADCIONA MAIS ALGUNS PONTOS NA INTELIGÊNCIA E TAMBÉM FAZ O TEMPO AVANÇAR...
        self.mostraAcao('lendo')
        relogio.avancaTempo(35)
        self.inteligência += 2
    
    def morrer(self): #FUNÇÃO MORRER SERVE PARA QUANDO O JOGADOR ESTÁ SEM ENERGIA OU COM MUITA FOME OU SEDE.
        if self.fome == 10:
            print('Sua fome atingiu nivel 10')
        if self.sede == 10:
            print('Sua sede atingiu nivel 10')
        if self.energia == 0:
            print('Sua energia atingiu nivel 0')
        if self.saúde == 0:
            print('Sua saúde atingiu nivel 0')
        print('FIM DO JOGO, VOCÊ MORREU :X ')
    
    #NAS FUNÇÕES ABAIXO NÓS TEMOS TODAS AS AÇOES DO PERSONAGEM... 
    # E TODAS ELAS SEGUEM O MESMO MODELO:... 
    # AO SER ACIONADAS ELAS ALTERAM OS ATRIBUTOS OU PRINTAM ALGO NA TELA.

    def comer(self):
        relogio.avancaTempo(35)
        if self.fome >= 2:
            self.mostraAcao('comendo')
            self.fome -= 2
            if self.saúde < 10:
                self.saúde += 1
            self.comida -= 2 
        elif self.fome == 0:
            print('\033[33mVOCÊ NÃO ESTÁ COM FOME.\033[04;37m')
        else:
            if self.saúde == 1:
                self.mostraAcao('comendo')
                self.fome -= 1
            if self.saúde < 10:
                self.saúde += 1
            self.comida -= 2 
        if self.fome >= 7:
            print('SE VOCÊ NÃO SE ALIMENTAR IRÁ MORRER')
        
    def beber(self):
        relogio.avancaTempo(5)
        if self.sede >= 2:
            self.mostraAcao('bebendo água')
            self.sede -= 2
            if self.saúde < 10:
                self.saúde += 1
            self.comida -= 2 
        elif self.sede == 0:
            print('\033[33mVOCÊ NÃO ESTÁ COM SEDE.\033[04;37m')
        else:
            if self.saúde == 1:
                self.mostraAcao('bebendo água')
                self.sede -= 1
            if self.saúde < 10:
                self.saúde += 1
            self.comida -= 2 
        if self.sede >= 7:
            print('SE VOCÊ NÃO BEBER ÁGUA IRÁ MORRER')
    
    def comprar(self):
        relogio.avancaTempo(60)
        self.mostraAcao('comprando')
        self.energia -= 0.5
        self.dinheiro -= 100
        self.comida += 2
    
    def trabalhar(self):
        relogio.avancaTempo(540)
        self.mostraAcao('trabalhando')
        self.energia -= 2
        self.fome += 1
        self.sede += 1
        self.saúde -= 1
        self.dinheiro += 1200
    
    def soneca(self):
        self.mostraAcao('tirando um cochilo')
        relogio.avancaTempo(30)
        self.energia += 5
        self.fome += 1
    
    def remedio1(self):
        relogio.avancaTempo(2)
        if self.saúde < 10:
            self.mostraAcao('tomando rémedio')
            self.saúde += 1
            self.remedio -= 1
        else:
            print('SUA SAÚDE JÁ ESTÁ EM 100%.')
    
    def dormir(self):
        self.mostraAcao('dormindo')
        relogio.avancaTempo(540)
        self.saúde += 2
        self.energia = 0
        self.energia = 20
        if self.fome == 5:
            self.fome += 5
    
#AMBIENTES EM QUE O JOGADOR PODE ENTRAR E ESCOLHER AS SUAS AÇÕES:

    def map(self):
        while not self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:  
            opcao = int(input('''ESTES SÃO SEUS AMBIENTES:
            [ 1 ]  CASA
            [ 2 ]  TRABALHO
            [ 3 ]  MERCADO
            [ 4 ]  MOSTRAR SEUS ATRIBUTOS
            [ 0 ]  SAIR
            --> : '''))
            if opcao == 1 :
                print("São "+str(relogio)+". ")
                self.casa()
            elif opcao == 2:
                print("São "+str(relogio)+". ")
                self.trabalho()
            elif opcao == 3:
                print("São "+str(relogio)+". ")
                self.mercado()
            elif opcao == 4:
                print("São "+str(relogio)+". ")
                self.dados()
            elif opcao == 0:
                print("São "+str(relogio)+". ")
                break
            else:
                print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE... ') 
        if self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
            self.morrer()   

    def casa(self):
        while not self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
            casa = int(input(f'''SÃO {(relogio)}  E ESSAS SÃO SUAS OPÇÕES NA CASA:

            [ 1 ] COMER
            [ 2 ] BEBER ÁGUA
            [ 3 ] TOMAR REMÉDIO
            [ 4 ] LER UM LIVRO
            [ 5 ] TIRAR UMA SONECA
            [ 6 ] DORMIR
            [ 7 ] MOSTRAR SEUS ATRIBUTOS
            [ 0 ] VOLTAR
            --> : '''))
            if casa == 1 :
                self.comer()
            elif casa == 2:
                self.beber()   
            elif casa == 3:
                self.remedio1()   
            elif casa == 4:
                self.ler()    
            elif casa == 5:
                self.soneca()  
            elif casa == 6:
                self.dormir()
            elif casa == 7:
                self.dados()
            elif casa == 0:
                break
            else:
                print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE... ')
        if self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
            self.morrer()
    
    def trabalho(self):
        if self.fome <= 8 and self.sede <= 8 and self.saúde >= 2 and self.energia >= 3:
            print('-=' * 30)
            print('Você chegou ao trabalho')
            print('-=' * 30)
            self.trabalhar()
            print('-=' * 30)
            print("Fim do expediente! Escolha para onde ir\n")
            self.dinheiro += 1
            print("São "+str(relogio)+". ")
        else:
            print('''VOCÊ NÃO PODE TRABALHAR: SUAS ATRIBUÍÇÕES VITAIS ESTÃO MUITO BAIXA
            VEJA OS TEUS ATRIBUTOS''')

    def mercado(self):
        print('VOCÊ CHEGOU AO MERCADO!')
        
        ce = 0
        ag = 0
        while True:
            relogio.avancaTempo(10)
            per = int(input('''
            
            TEMOS AS OPÇÕES ABAIXO:
            [ 1 ]    CESTA BÁSICA ......................R$ 80,00
            [ 2 ]    FARDO COM 8 GARRAFAS DE ÁGUA.......R$ 15,00
            [ 3 ]    FINALIZAR A COMPRA
            [ 4 ]    NÃO/VOLTAR
            --> : '''))
            somar = ce * 80.0 + ag * 15.0
            if per == 1:
                ce += 1
            elif per == 2:
                ag +=1
            elif per == 3:
                #print(ce, ag)
                per1 = int(input(f'''
                O VALOR TOTAL DE SUA COMPRA É DE R$ {somar:.2f}
                DESEJA CONTINUAR?
                [ 1 ] SIM
                [ 2 ] NÃO
                '''))
                if per1 == 1 and self.dinheiro < somar :
                    print(f'''
                    VOCÊ NÃO TEM DINHEIRO SUFICIENTE PARA FINALIZAR SUA COMPRA
                    SEU SALDO ATUAL É DE R$ {self.dinheiro:.2f}
                    ''')
                    print("São "+str(relogio)+". ")
                    print( self.map())
               
                elif per1 == 1 :
                    self.comprar()
                    print('OBRIGADA E VOLTE SEMPRE!')
                    print("São "+str(relogio)+". ")
                    print( self.map())

            elif per  == 4 :
                print( self.map())              

                    
            else:
                print('OPÇÃO INVÁLIDA')
