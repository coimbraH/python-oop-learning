from rich import print
class Diario:
    def __init__(self, senha = ''):
        self.__segredos = []
        self.__senha = senha

    @property
    def senha(self):
        return self.senha
    @senha.setter
    def senha(self, senha):
        if senha != self.__senha:
            raise PermissionError('Senha incorreta. Você não pode ver meu diário.')

    def escrever(self, msg):
        return self.__segredos.append(f'{msg}')

    def ler(self,senha=None):
        self.senha = senha
        print(f'[green]Diário LIBERADO[/]')
        for i in self.__segredos:
            print(f'- {i}')

