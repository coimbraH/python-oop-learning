#Crie a classe Funcionario, onde podemos cadastrar NOME, SETOR, e CARGO.
#Crie também um metodo que permita ao funcionário se apresentar
from rich import print
from rich import inspect

class Funcionario:
    empresa = 'OkOkO'
    def __init__(self, nome = '', setor = '', cargo = ''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá eu sou [cyan]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'


c1 = Funcionario('Henrique', 'TI', 'diretor' )
print(c1.apresentacao())

c2 = Funcionario('Maria', 'TI', 'programador')
print(c2.apresentacao())

# inspect(c1, methods=True, dunder=True)