class Steve:
    def __init__(self):
        self.energy = 10
        self.hungr = 0
        self.thirst = 0
        self.forca = 0
        self.dinheiro = 0
        self.smart = 0
        self.depression = 0

    #def decor():
        #print('-='*20)

    def die(self):
        if self.energy == 0 or self.hungr == 20 or self.thirst == 20 or self.depression == 20:
            print('Game Over!')

    def study(self):
        self.hungr += 1
        self.thirst += 1
        self.energy -= 1
        if self.smart < 57:
            self.smart += 3
        elif self.smart < 60:
            self.smart +=1
        #self.decor()
        print(f'''
        Sua energia está em: {self.energy}
        Sua fome: {self.hungr}
        Sua sede: {self.thirst}
        Sua inteligência: {self.smart}''')

    


