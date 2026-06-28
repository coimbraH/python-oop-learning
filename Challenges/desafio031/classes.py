
class Retangulo:
    def __init__(self, base = 0, altura = 0):
        self._base = 0
        self._altura = 0
        self._area = 0

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, base = None):
        if base < 0:
            raise ValueError('Valor inválido para base')
        self._base = base
        self._area = self._altura * self._base

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, altura = None):
        if altura < 0:
            raise ValueError('Valor inválido para altura')
        self._altura = altura
        self._area = self._altura*self._base

    @property
    def area(self):
        return self.base*self.altura

    @property
    def medidas(self):
        return
    @medidas.setter
    def medidas(self,tupla):
        if tupla[0] < 0 or tupla[1] < 0 :
            raise ValueError('Valor inválido para altura ou base')
        print(f'Base = {tupla[0]}\nAltura = {tupla[1]}\nArea = {tupla[0] * tupla[1]}')







