from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, qtd_lados = 0):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.qtd_lados * self.lado

    def area(self):
        return self.lado**2

class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(1)
        self.raio = raio

    def perimetro(self):
        return 2*3.14159*self.raio

    def area(self):
        return 3.14159 * self.raio**2
