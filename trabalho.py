from relogio import Relogio
relogio = Relogio()

import time


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

# daqui pra baixo é o código que o gabriel precisa juntar ao arquivo  
    
    def trabalho(self):
        print('-=' * 30)
        print('Você chegou ao trabalho')
        for i in range(3):
            time.sleep(2)
            print('Trabalhando...')
        print("Fim do expediente!")
        self.dinheiro += 1
        relogio.avancaTempo(480)


persona = Steve()
print(persona.dinheiro)
persona.trabalho()
print(relogio.horas)