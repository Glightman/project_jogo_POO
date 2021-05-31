class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
        self.dia = 1
    
    def __str__(self): 
        return f"{self.horas:02d}:{self.minutos:02d} do dia {self.dia:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
            if self.horas >= 24:
                self.horas = 0
                self.dia +=1


