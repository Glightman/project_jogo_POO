class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self): # Pesquisar significado dessa função especifica.
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
       

    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))