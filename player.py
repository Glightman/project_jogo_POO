class Steve:
    def __init__(self):
        self.energia = 10
        self.fome = 5
        self.sede = 5
        self.saúde = 10
        self.dinheiro = 0
        self.inteligência = 5
        self.depressão = 0
        self.comida = 10
    def dados(self):
        print(f'''
        Você no momento esta com:
        [{self.energia}/20]  de Energia
        [{self.sede}/10]  de Sede
        [{self.fome}/10]  de Fome
        [{self.saúde}/10]  de Saúde
        [{self.dinheiro}/10]  de Dinheiro
        [{self.inteligência}/10]  de Inteligência
        [{self.comida}/ 10]  de Alimentos em casa    
        
        ''')
    print(dados)

    #def alimento(self ):
     #  self.comida -= 2
   
      
    
    
    def Comer( self):
        self.fome -= 2
        self.saúde += 0.5
        self.comida -= 2     
    
    def Beber (self):
        self.sede -= 2
        self.saúde += 0.5
       
    def Estudar(self):
        self.energia -= 4
        self.fome += 2
        self.sede += 2
        self.inteligência += 3
    def Malhar (self):
        self.energia -= 3
        self.fome += 2
        self.sede += 2 
        self.saúde += 2
    def Comprar(self):
        self.energia -= 0.5
        self.dinheiro -= 100
        self.comida += 2
    def Trabalhar(self):
        self.energia -= 2
        self.fome += 1
        self.sede += 1
        self.saúde -= 1
        self.dinheiro += 120
          
    def casa(self):
        while True:
            casas = int(input('''ESSAS SÃO SUAS OPÇÕES NA CASA:
            [ 1 ] COMER
            [ 2 ] BEBER ÁGUA
            [ 3 ] TOMAR REMÉDIO
            [ 4 ] LER UM LIVRO
            [ 5 ] TIRAR UMA SONECA
            [ 6 ] DORMIR
            [ 0 ] VOLTAR
            --> : '''))
            if casas == 0:
                break
           
            
    



 
  
  

