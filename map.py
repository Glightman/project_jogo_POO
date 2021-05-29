from player import Steve
class Map:
    def __init__(self):
        self.casa
        self.bar
        self.mercado
        self.escola
        self.restaurante
        self.trabalho
        self.academia

    def casa(self):
        while not self.fome == 10 or self.sede == 10 or self.energia == 0 or self.saúde == 0:
            opt = int(input('''ESSAS SÃO SUAS OPÇÕES NA CASA:
            [ 1 ] COMER
            [ 2 ] BEBER ÁGUA
            [ 3 ] TOMAR REMÉDIO
            [ 4 ] LER UM LIVRO
            [ 5 ] TIRAR UMA SONECA
            [ 6 ] DORMIR
            [ 7 ] MOSTRAR SEUS ATRIBUTOS
            [ 0 ] VOLTAR
            --> : '''))
            if opt == 1 :
                Steve.comer
            elif opt == 2:
                Steve.beber  
            elif opt == 3:
                Steve.remedio   
            elif opt == 4:
                Steve.ler    
            elif opt == 5:
                Steve.soneca 
            elif opt == 6:
                Steve.dormir
            elif opt == 7:
                Steve.dados
            else:
                self.decor()
                print('VOCÊ SAIU DO JOGO')
                self.decor()
                break
        self.morrer()