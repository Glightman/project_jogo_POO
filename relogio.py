class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self): 
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    def hora(self, horas):
        self.horas += horas
        while(self.horas >= 24):
            self.horas -= 24
            self.dias += 1
       
