from abc import ABC, abstractmethod
from rich import table

# se o frete for de moto , a distancia é livre , não tem distancia minima nem maxima
# pro caminhão o frete minimo é 50km de viagem
# e pra drone o máximo é 10km entrega

class Transporte(ABC):
    def __init__(self, dist = 0):
        self.distancia = dist
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 0.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f'R${self.frete:.2f}'

class Caminhao(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 1.20

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        if self.distancia >= 50:
            return f'R${self.frete:.2f}'
        else:
            return 'Caminhão só sai da garagem em fretes acima de 50km'

class Drone(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 9.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        if self.distancia <= 10:
            return f'R${self.frete:.2f}'
        else:
            return 'A distância máxima de fretes com drone é 10km'