from relogio import Relogio
relogio = Relogio()
class Steve:
    def __init__(self):
        self.energia = 10
        self.fome = 5
        self.sede = 5
        self.saúde = 10
        self.dinheiro = 0
        self.inteligência = 5
        self.comida = 10
        self.remedio = 10

     #AÇÕES ATRIBUÍDAS AO JOGADOR:

    def dados(self):
        return f'''           \033[1m\033[33mSEUS ATRIBUTOS SÃO:\033[04;37m
        \033[1m\033[04;37m[ENERGIA      -->  {self.energia}/20]
        [SEDE         -->  {self.sede}/10]
        [FOME         -->  {self.fome}/10]
        [SAÚDE        -->  {self.saúde}/10]
        [DINHEIRO     -->  {self.dinheiro}/10]
        [INTELÍGÊNCIA -->  {self.inteligência}/10]
        [SUPRIMENTOS  -->  {self.comida}/ 10]\033[04;37m'''
    
    def decor(self):
        print('-='*30)
    
    def ler(self):
        relogio.avancaTempo(35)
        self.inteligência += 2
    
    def morrer(self):
        if self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
            print('FIM DO JOGO, VOCÊ MORREU :X ')
    
    def beberVinho(self):
        relogio.avancaTempo(40)
        self.energia += 1
        self.saúde += 1    
    
    def comer(self):
        relogio.avancaTempo(35)
        self.fome -= 2
        self.saúde += 0.5
        self.comida -= 2   
        if self.fome == 9:
            print('SE VOCÊ NÃO SE ALIMENTAR IRÁ MORRER')  
      
    def beber(self):
        relogio.avancaTempo(5)
        if self.sede > 1 :
            self.sede -= 2
            self.saúde += 0.5
        elif self.sede == 1 :
            self.sede -= 1
        else:
            print('VOCÊ NÃO ESTÁ COM SEDE.')
        
    def estudar(self):
        relogio.avancaTempo(240)
        self.energia -= 4
        self.fome += 2
        self.sede += 2
        self.inteligência += 3
    
    def malhar(self):
        relogio.avancaTempo(60)
        self.energia -= 3
        self.fome += 2
        self.sede += 2 
        self.saúde += 2
    
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
        self.dinheiro += 120
    
    def soneca(self):
        relogio.avancaTempo(30)
        self.energia += 5
    
    def remedio(self):
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
            [ 2 ]  BAR
            [ 3 ]  MERCADO
            [ 4 ]  ESCOLA
            [ 5 ]  RESTAURANTE
            [ 6 ]  TRABALHO
            [ 7 ]  ACADEMIA
            [ 0 ]  SAIR
            --> : '''))
            if opcao == 1 :
                self.casa()
            elif opcao == 2:
                self.bar()
        self.morrer()   

    def casa(self):
        while not self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
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
                self.remedio()   
            elif casa == 4:
                self.ler()    
            elif casa == 5:
                self.sono()  
            elif casa == 6:
                self.dormir()
            elif casa == 7:
                print(self.dados())
            else:
                self.decor()
                print('VOCÊ SAIU DO JOGO')
                self.decor()
                break
        self.morrer()

    def bar(self):
        while True:
            per = int(input('''SEJA BEM VINDO
            TEMOS APENAS VINHO EM NOSSO CARDÁPIO.
            POSSO SERVI LO
            [ 1 ] SIM
            [ 2 ] MOSTRAR SEUS ATRIBUTOS
            [ 3 ] NÃO/SAIR
            '''))
            if per == 1:
                self.beberVinho()
            elif per == 2:
                self.dados()
            else:
                break

    def mercado(self):
        per = int(input('''VOCÊ CHEGOU AO MERCADO!
        O TOTAL DE SUA COMPRA É DE R$ 100,00
        DESEJA EFETUAR A COMPRA?
        [ 1 ] SIM
        [ 2 ] MOSTRAR SEUS ATRIBUTOS
        [ 3 ] NÃO/VOLTAR
        --> : '''))
        if self.dinheiro < 100 :
            print('VOCÊ NÃO TEM DINHEIRO SUFICIENTE PARA FINALIZAR SUA COMPRA')
    
    def escola(self):
        parar = 0
        while parar == 0:
            opt = int(input('''SEJA BEM VINDO AO PY'SCHOOL
            [ 1 ] Estudar
            [ 2 ] Beber água
            [ 3 ] Voltar
            --> : '''))
            if opt == 1:
                self.estudar
            elif opt == 2:
                self.beber
            elif opt == 3:
                parar += 1
            else:
                print('Esta opção não é válida, tente outra: ')

    def academia(self):
            parar = 0
            while parar == 0:
                opt = int(input('''SEJA BEM VINDO A ACADEMIA PY'FIT
                    [ 1 ] Malhar
                    [ 2 ] Beber água
                    [ 3 ] Mostrar atributos
                    [ 4 ] Voltar
                    --> : '''))
                if opt == 1:
                    self.malhar
                elif opt == 2:
                    self.beber
                elif opt == 3:
                    self.dados
                elif opt == 4:
                    parar += 1
                else:
                    print('Esta opção não é válida, tente outra: ')
