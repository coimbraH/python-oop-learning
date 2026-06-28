from rich import print, inspect

class Termostato:
    def __init__(self):
        self.temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp): #validar temperatura acima de 16 e abaixo de 30, e fazendo de 0,5 em 0,5
        if temp%0.5 != 0:
            raise ValueError(f'Temperatura de {temp} é inválido')
        if temp < 16:
            self.__temperatura = 16
        elif temp > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = temp

    @property
    def ftemperatura(self): #retornar temperatura formatada com graus centigrados
        return f'{self.__temperatura}°C'