from relogio import Relogio
from time import sleep
relogio = Relogio()
dia = 1
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

     #AÇÕES ATRIBUÍDAS AO JOGADOR: ABAIXO NÓS TEMOS TODAS AS AÇÕES QUE O JOGADOR PODE FAZER EM CADA AMBIENTE.

    def dados(self): #ESSE MÉTODO MOSTRA OS ATRIBUTOS DO PERSONAGEM, ASSIM ELE PODE ACOMPANHAR SUA VIDA E TOMAR DECISÕES BASEADAS NESSAS INFORMAÇÕES.
        #NESTA LINHA ABIXO NÓS TEMOS UM PRINT DOS ATRIBUTOS, O CÓDIGO ANTES E DEPOIS DO TEMA SERVE PARA COLORIR O TEXTO QUE SERÁ MOSTRADO NO TERMINAL, ALÉM DE COLOCAR AS LETRAS EM NEGRITO TAMBÉM.
        #NÓS TAMBÉM USAMOS O f' PARA MOSTRAR OS ATRIBUTOS DIRETAMENTE DA VARIÁVEL.
        print(f'''           \033[1m\033[33mSEUS ATRIBUTOS SÃO:\033[04;37m
        \033[1m\033[04;37m[ENERGIA      -->  {self.energia}/20]
        [SEDE         -->  {self.sede}/10]
        [FOME         -->  {self.fome}/10]
        [SAÚDE        -->  {self.saúde}/10]
        [DINHEIRO     -->  {self.dinheiro}/10]
        [INTELÍGÊNCIA -->  {self.inteligência}/10]
        [SUPRIMENTOS  -->  {self.comida}/ 10]
        [REMÉDIOS     -->  {self.remedio}/10]\033[04;37m''')
    
    def decor(self): #ESTA FUNÇÃO SERVE PARA DECORAR NOSSO TEXTO NO TERMINAL 
        print('-='*30) #ESSE PRINTE FARA UMA LINHA IGUAL A ESSA -->: -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def ler(self): #A FUNÇÃO LER OU AÇÃO LER, ADCIONA MAIS ALGUNS PONTOS NA INTELIGÊNCIAE TAMBÉM FAZ O TEMPO AVANÇAR...
        relogio.avancaTempo(35)
        self.inteligência += 2
    
    def morrer(self): #FUNÇÃO MORRER SERVE PARA QUANDO O JOGADOR ESTÁ SEM ENERGIA OU COM MUITA FOME OU SEDE.
        if self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
            print('FIM DO JOGO, VOCÊ MORREU :X ')
    
    #NAS FUNÇÕES ABAIXO NÓS TEMOS TODAS AS AÇOES DO PERSONAGEM... 
    # E TODAS ELAS SEGUEM O MESMO MODELO:... 
    # AO SER ACIONADAS ELAS ALTERAM OS ATRIBUTOS OU PRINTAM ALGO NA TELA.

    def comer(self):
        relogio.avancaTempo(35)
        self.fome -= 2
        self.saúde += 0.5
        self.comida -= 2   
        if self.fome == 9:
            print('SE VOCÊ NÃO SE ALIMENTAR IRÁ MORRER')
        str = '''o Steve está comendo
        '''
        for ch in str: 
            sleep(0.1) 
            print(ch, end='', flush=True)
        sleep(1)
        print('-='*30)
        str = '''Você acabou de comer! 
        \033[33mCONFIRA SEUS ATRIBUTOS\033[04;37m
        '''
        for ch in str: 
            sleep(0.1) 
            print(ch, end='', flush=True)
        #self.dados()

    def beber(self):
        relogio.avancaTempo(5)
        if self.sede > 1 :
            self.sede -= 2
            self.saúde += 0.5
        elif self.sede == 1 :
            self.sede -= 1
        else:
            print('\033[33mVOCÊ NÃO ESTÁ COM SEDE.\033[04;37m')
    
    def Comprar(self):
        relogio.avancaTempo(60)
        self.energia -= 0.5
        self.dinheiro -= 100
        self.comida += 2
    
    def Trabalhar(self):
        relogio.avancaTempo(540)
        self.energia -= 2
        self.fome += 1
        self.sede += 1
        self.saúde -= 1
        self.dinheiro += 1200
    
    def soneca(self):
        relogio.avancaTempo(30)
        self.energia += 5
        self.fome += 1
    
    def remedio1(self):
        relogio.avancaTempo(2)
        self.saúde += 1
        self.remedio -= 1
    
    def dormir(self):
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
            [ 2 ]  RESTAURANTE
            [ 3 ]  MERCADO
            [ 4 ]  ESCOLA
            [ 5 ]  BAR
            [ 6 ]  TRABALHO
            [ 7 ]  ACADEMIA
            [ 0 ]  SAIR
            --> : '''))
            if opcao == 1 :
                print("São "+str(relogio)+" do dia "+str(dia)+". ")
                self.casa()
            elif opcao == 2:
                print("São "+str(relogio)+" do dia "+str(dia)+". ")
                self.restaurante()
            elif opcao == 3:
                print("São "+str(relogio)+" do dia "+str(dia)+". ")
                self.mercado()
            elif opcao == 4:
                print("São "+str(relogio)+" do dia "+str(dia)+". ")
                self.escola()
            elif opcao == 5:
                print("São "+str(relogio)+" do dia "+str(dia)+". ")
                self.bar()
            elif opcao == 6:
                print("São "+str(relogio)+" do dia "+str(dia)+". ")
                self.trabalho()
        self.morrer()   

    def casa(self):
        while not self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
            print('-='*30)
            if self.fome == 9:
                str = '''\033[1m\033[32m!!! SE NÃO SE ALIMENTAR VOCÊ IRÁ MORRER !!!\033[37m
                '''
                for ch in str: 
                    sleep(0.07) 
                    print(ch, end='''''', flush=True)
            print('-='*30)
            casa = int(input('''ESSAS SÃO SUAS OPÇÕES NA CASA:
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
            else:
                self.decor()
                print('VOCÊ SAIU DO JOGO')
                self.decor()
                break
        self.morrer()
    
    def trabalho(self):
        import time

        print('-=' * 30)
        print('Você chegou ao trabalho')
        for i in range(3):
            time.sleep(2)
            print('Trabalhando...')
        print("Fim do expediente! Escolha para onde ir\n")
        self.dinheiro += 1
        self.Trabalhar()
        print("São "+str(relogio)+" do dia "+str(dia)+". ")

    def mercado(self):
        print('VOCÊ CHEGOU AO MERCADO!')
        
        ce = 0
        ag = 0
        while True:
            per = int(input('''
            
            TEMOS AS OPÇÕES ABAIXO:
            [ 1 ]    CESTA BÁSICA ......................R$ 80,00
            [ 2 ]    FARDO COM 8 GARRAFAS DE ÁGUA.......R$ 15,00
            [ 3 ]    FINALIZAR A COMPRA
            [ 4 ] NÃO/VOLTAR
            --> : '''))
            somar = (ce * 80.0) + ( ag * 15.0)
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
                if per1 == 1 :
                    if self.dinheiro < somar :
                        per2 = int(input(f'''
                    VOCÊ NÃO TEM DINHEIRO SUFICIENTE PARA FINALIZAR SUA COMPRA
                    SEU SALDO ATUAL É DE R$ {self.dinheiro:.2f}
                    DESEJA REVER O PEDIDO?
                    [ 1 ] SIM
                    [ 2 ] NÃO
                    '''))
                    if per2 == 1 :
                       ce = 0
                       ag = 0
                    else:
                        print('OBRIGADA E VOLTE SEMPRE!')
            elif per  == 4 :
                print( self.map())              

                    
            else:
                print('OPÇÃO INVÁLIDA')
