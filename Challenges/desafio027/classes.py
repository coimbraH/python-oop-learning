from abc import ABC, abstractmethod
from rich import print, inspect
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome='', vida = 0, golpes = 0):
        self.nome = ''
        self.vida = 0
        self.golpes = 0

    def atacar(self,alvo,forca):
        self.alvo = alvo
        self.golpes = forca
        dano = randint(0, self.golpes)
        print(f'{self.nome}({self.vida}) atacou {self.alvo.nome}({self.alvo.vida}) com {choice(self.magias)} de força {dano}')
        self.receber_dano(dano)
        print(f'O jogador {self.alvo.nome} recebeu {dano} de dano e agora sua vida é de {self.alvo.vida} ')

    def receber_dano(self,dano):
        self.alvo.vida -= dano

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.nome = f'[yellow]{nome}[/]'
        self.vida = vida
        self.magias = ['Técnica dos Mil Punhos', 'Corte Preciso', 'Fúria Cega']

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f'{self.nome} enrolou atadura nos ferimentos e recuperou {cura} pontos de vida.  Sua vida é de {self.vida}')

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome,vida)
        self.nome = f'[purple]{nome}[/]'
        self.vida = vida
        self.magias = ['Bola de Fogo', 'Raio de Gelo', 'Relâmpago']
    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f'{self.nome} fez uma magia de cura e recuperou {cura} pontos de vida. Sua vida é de {self.vida}')