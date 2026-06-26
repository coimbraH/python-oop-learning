#crie uma classe chamada GAMER, onde podemos cadastrar o
#NOME, NICK e os JOGOS FAVORITOS de uma pessoa.
#Crie também um metodo que permita mostrar a ficha gamer

from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, nome='',nick=''):
        self.nome = nome
        self.nick = nick
        self.fav = []

    def add_favoritos(self, n):
        self.fav.append(n)

    def jogo(self):
        jogos = ''
        for n in sorted(self.fav):
            jogos += f':video_game: {n} \n'
        return jogos

    def ficha(self):
        x = Panel(
        f'Nome real: {self.nome}\n'
        f'Jogos favoritos:\n'
        f'{self.jogo()}',
        width=50,
        title=self.nick,
        )
        print(x)

j1 = Gamer("Henrique Coimbra", "OkOkO1337")
j1.add_favoritos('Super Maior World')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of War')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer('Filipe Albino', 'Pipi Gamer')
j2.add_favoritos('Roblox')
j2.add_favoritos('Fifa 2026')
j2.ficha()