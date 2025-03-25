from semente import Semente

class Flor():
    def __init__(self, semente):
        self.semente = semente
    
    def florescer(self):
        if self.semente.nutrida:
            print(f'Depois de um longo tempo, a semente se tornou uma linda flor de {self.semente.tipo}\n')
        else:
            print('A semente ainda não está nutrida!\n')

semente = Semente('Violeta')
semente.plantarSemente()
semente.nutrirSemente()

flor = Flor(semente)
flor.florescer()

