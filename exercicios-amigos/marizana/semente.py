class Semente():
    def __init__(self, tipo):
        self.tipo = tipo
        self.plantada = False
        self.nutrida = False

    def plantarSemente(self):
        self.plantada = True
        print(f'\nPlantando semente de {self.tipo}')
    
    def nutrirSemente(self):
        if self.plantada:
            self.nutrida = True
            print('A semente bonita toma sol e água todos os dias!')